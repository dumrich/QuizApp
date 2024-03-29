from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, SaveUserInstance, UserAnswer
from .forms import QuizForm, QuestionForm
from random import shuffle
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from itertools import combinations
from collections import defaultdict
import ast
from django.contrib.auth.decorators import login_required


def turn_to_model(file, quiz, request):
    file = ast.literal_eval(file.read().decode('latin'))
    for i in range(1, len(file.keys())+1):
        question = file["Q"+str(i)]
        question_question = question.get("question")
        question_question_type = question.get("question_type")
        question_answer = question.get("answer")
        question_choice_2 = question.get("choice_2")
        question_choice_3 = question.get("choice_3", "n/a")
        question_choice_4 = question.get("choice_4", "n/a")
        quiz.questions.create(question=question_question, question_type=question_question_type, answer=question_answer,
                              choice_2=question_choice_2, choice_3=question_choice_3, choice_4=question_choice_4)
    return redirect(request.path_info)


def handle_form(request):
    query = int(request.POST["playId"])
    quiz = get_object_or_404(Quiz, playId=query)
    return redirect(f'/{quiz.playId}/{quiz.slug}')


def quiz_render_pdf_view(request, *args, **kwargs):
    '''
    render a pdf
    '''
    pk = kwargs.get('pk')
    quiz_instance = get_object_or_404(SaveUserInstance, pk=pk)

    template_path = 'quiz/pdf.html'
    context = {'quiz_instance': quiz_instance}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required
def QuizListView(request):
    '''
    List all quizzes
    '''
    queryset = Quiz.objects.all()
    if request.method == "POST":
        try:
            if request._post['playId']:
                return handle_form(request)
        except KeyError:
            pass
    return render(request, 'quiz/list.html', {'quizzes': queryset})


def quiz_take(request, pk, slug):
    '''
    Take a quiz
    '''
    quiz = get_object_or_404(Quiz, slug=slug, playId=pk)

    if request.method == "POST":
        try:
            if request._post['playId']:
                return handle_form(request)
        except:
            pass

    questions = list(quiz.questions.all())
    shuffle(questions)
    question_order_dict = defaultdict(dict)
    for question in questions:
        if question.question_type == "MC" or question.question_type == "D":
            question_order_dict[question] = {question.answer: question.answer, question.choice_2: question.choice_2,
                                             question.choice_3: question.choice_3, question.choice_4: question.choice_4}
            question_order_list = list(question_order_dict[question].items())
            shuffle(question_order_list)
            question_order_dict[question] = dict(question_order_list)
    questions = questions[:5]

    context_dict = {'quiz': quiz,
                    'questions': questions,
                    'question_order_dict': question_order_dict,
                    }

    if request.method == 'POST':
        questions = list(dict(request.POST).items())[:-1]
        answers = []
        for question in questions:
            stripped_question = question[0].split('/')[0]
            answer = UserAnswer.objects.create(user=request.user, quiz=quiz, question=quiz.questions.get(question=stripped_question),
                                               answer=question[1][0])
            answers.append(answer)
        if SaveUserInstance.objects.filter(user=request.user, quiz=quiz):
            attempts = list(SaveUserInstance.objects.filter(
                user=request.user, quiz=quiz))[-1].attempt + 1
        else:
            attempts = 1
        score = 0

        for thing in answers:
            if thing.question.answer == thing.answer:
                score = score + 1
            else:
                continue
        UserInstance = SaveUserInstance.objects.create(
            user=request.user, quiz=quiz, attempt=attempts, score=score)
        UserInstance = UserInstance.UserAnswer.add(*answers)
        UserInstance = SaveUserInstance.objects.get(
            user=request.user, quiz=quiz, attempt=attempts, score=score)
        return redirect(f'/{quiz.playId}/{quiz.slug}/{UserInstance.attempt}')

    return render(request,
                  'quiz/quiz.html',
                  context_dict
                  )


def quiz_detail(request, pk, slug):
    '''
    View a Quiz in depth
    '''
    quiz = get_object_or_404(Quiz, playId=pk, slug=slug)
    attempts = len(SaveUserInstance.objects.filter(
        quiz=quiz, user=request.user))

    if request.method == "POST":
        try:
            if request._post['playId']:
                return handle_form(request)
        except:
            pass
    return render(request,
                  'quiz/detail.html',
                  {'quiz': quiz,
                   'attempts': attempts})


def instance_detail(request, pk, slug, attempt):
    '''
    View quiz results
    '''
    quiz = get_object_or_404(Quiz, playId=pk, slug=slug)
    quiz_instance = get_object_or_404(
        SaveUserInstance, quiz=quiz, user=request.user, attempt=attempt)
    total_questions = len(quiz_instance.UserAnswer.all())
    if request.method == "POST":
        try:
            if request._post['playId']:
                return handle_form(request)
        except:
            pass
    return render(request,
                  'quiz/instance.html',
                  {'quiz_instance': quiz_instance,
                   'total_questions': total_questions})


def quiz_create(request):
    '''
    Quiz results
    '''
    if request.method == "POST":
        try:
            if request._post['playId']:
                return handle_form(request)
        except:
            pass
    new_quiz = None
    if request.method == 'POST':
        quiz_form = QuizForm(data=request.POST)
        if quiz_form.is_valid():
            new_quiz = quiz_form.save(commit=False)
            new_quiz.author = request.user
            new_quiz.save()
            return redirect("/")
    else:
        quiz_form = QuizForm()

    return render(request,
                  'quiz/create.html',
                  {'quiz_form': quiz_form,
                   'new_quiz': new_quiz})


def quiz_delete(request, pk, slug):
    Quiz.objects.get(playId=pk, slug=slug).delete()
    return redirect('/')


def quiz_edit(request, pk, slug):
    quiz = get_object_or_404(Quiz, playId=pk, slug=slug)
    questions = quiz.questions.all()
    new_question = None
    if request.method == "POST":
        if file:=request.FILES.get('file', 0):
            file=request.FILES.get('file', 0)
            return turn_to_model(file, quiz, request)
        if request._post.get("delete", 0):
            quiz.questions.get(id=int(request._post["delete"])).delete()
            return HttpResponseRedirect(request.path_info)
        if request._post.get('playId', 0):
            return handle_form(request)
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            if new_question.question_type == 'TF':
                new_question.choice_3 = None
                new_question.choice_4 = None
            new_question.quiz = quiz
            new_question.save()
            return redirect(f'/{quiz.playId}/{quiz.slug}/edit/')
    else:
        question_form = QuestionForm()

    return render(request,
                  'quiz/edit.html',
                  {'quiz': quiz,
                   'questions': questions,
                   'new_question': new_question,
                   'question_form': question_form,
                   })
