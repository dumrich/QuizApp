from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Quiz, SaveUserInstance, UserAnswer
from .forms import QuizForm, QuestionForm
from random import shuffle
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


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


def QuizListView(request):
    '''
    List all quizzes
    '''
    queryset = Quiz.objects.all()
    if request.method == "POST":
        try:
            if request._post['playId']:
                return handle_form(request)
        except:
            pass
    return render(request, 'quiz/list.html', {'quizzes':queryset})
    

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
    print(questions) 

    shuffle(questions)
    print(questions)
    questions = questions[:5]
    
    

    if request.method == 'POST':
        questions= list(dict(request.POST).items())[:-1]
        answers = []
        for question in questions:
             stripped_question = question[0].split('/')[0]
             answer = UserAnswer.objects.create(user=request.user, quiz=quiz, question=quiz.questions.get(question=stripped_question),
                     answer=question[1][0])
             answers.append(answer)
        print(answers)
        if SaveUserInstance.objects.filter(user=request.user, quiz=quiz):
            attempts = list(SaveUserInstance.objects.filter(user=request.user, quiz=quiz))[-1].attempt + 1
        else:
            attempts = 1
        score = 0

        for thing in answers:
            if thing.question.answer == thing.answer:
                score = score + 1
            else:
                continue       
        print(score)
        UserInstance = SaveUserInstance.objects.create(user=request.user, quiz=quiz, attempt=attempts, score=score)
        UserInstance = UserInstance.UserAnswer.add(*answers)
        UserInstance = SaveUserInstance.objects.get(user = request.user, quiz=quiz, attempt=attempts, score = score)
        return redirect(f'/{quiz.playId}/{quiz.slug}/{UserInstance.attempt}')
        
    return render(request, 
                  'quiz/quiz.html',
                  {'quiz':quiz,
                   'questions': questions
                  })


def quiz_detail(request, pk, slug):
    '''
    View a Quiz in depth
    '''
    quiz = get_object_or_404(Quiz, playId=pk, slug=slug)
    attempts = len(SaveUserInstance.objects.filter(quiz=quiz, user=request.user))
    
    if request.method == "POST":
        try:
            if request._post['playId']:
                return handle_form(request)
        except:
            pass
    return render(request, 
                  'quiz/detail.html',
                  {'quiz':quiz,
                   'attempts':attempts})


def instance_detail(request, pk, slug, attempt):
    '''
    View quiz results
    '''
    quiz = get_object_or_404(Quiz, playId=pk, slug=slug)
    quiz_instance = get_object_or_404(SaveUserInstance, quiz=quiz, user=request.user, attempt=attempt)
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
                   'total_questions':total_questions})

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
                  {'quiz_form':quiz_form,
                   'new_quiz':new_quiz})


def quiz_delete(request, pk, slug):
    Quiz.objects.get(playId=pk, slug=slug).delete()
    return redirect('/')

def quiz_edit(request, pk, slug):
    quiz = get_object_or_404(Quiz, playId=pk, slug=slug)
    questions = quiz.questions.all()

    if request.method == "POST":
        try:
            if request._post['playId']:
                return handle_form(request)
        except:
            pass
    new_question = None
    if request.method=="POST":
        try:
            if request._post["delete"]:
                quiz.questions.get(id=request._post["delete"][0]).delete()
                return redirect('')
        except:
            pass
    if request.method == "POST":
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            if new_question.question_type=='TF':
                new_question.choice_3 = None
                new_question.choice_4 = None
            new_question.quiz = quiz
            new_question.save()
            return redirect(f'/{quiz.playId}/{quiz.slug}/edit/')
    else:
        question_form = QuestionForm()

    return render(request, 
                  'quiz/edit.html',
                  {'quiz':quiz,
                   'questions': questions,
                   'new_question': new_question,
                   'question_form': question_form})

