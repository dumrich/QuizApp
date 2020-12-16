from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Quiz, SaveUserInstance, UserAnswer
from .forms import QuizForm, QuestionForm
from random import shuffle


class QuizListView(ListView):
    queryset = Quiz.objects.all()
    context_object_name = 'quizzes'
    template_name = 'quiz/list.html'


def quiz_take(request, pk, slug):
    quiz = get_object_or_404(Quiz, slug=slug, pk=pk)
    
    questions = list(quiz.questions.all())
    

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
        print(SaveUserInstance.objects.get(user = request.user, quiz=quiz, attempt=attempts, score = score))
        
    return render(request, 
                  'quiz/quiz.html',
                  {'quiz':quiz,
                   'questions': questions
                  })


def quiz_detail(request, pk, slug):
    quiz = get_object_or_404(Quiz, pk=pk, slug=slug)
    
    questions = quiz.questions.all()

    new_question = None

    if request.method == "POST":
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            if new_question.question_type=='TF':
                new_question.choice_3 = None
                new_question.choice_4 = None
            new_question.quiz = quiz
            new_question.save()
    else:
        question_form = QuestionForm()

    return render(request, 
                  'quiz/detail.html',
                  {'quiz':quiz,
                   'questions': questions,
                   'new_question': new_question,
                   'question_form': question_form})

def instance_detail(request, pk, slug, attempt):
    quiz = get_object_or_404(Quiz, pk=pk, slug=slug)
    quiz_instance = get_object_or_404(SaveUserInstance, quiz=quiz, user=request.user, attempt=attempt)
    total_questions = len(quiz_instance.UserAnswer.all())
    return render(request,
                  'quiz/instance.html',
                  {'quiz_instance': quiz_instance,
                   'total_questions':total_questions})

    
def quiz_create(request):
    new_quiz = None
    if request.method == 'POST':
        quiz_form = QuizForm(data=request.POST)
        if quiz_form.is_valid():
            new_quiz = quiz_form.save(commit=False)
            new_quiz.author = request.user
            new_quiz.save()
    else:
        quiz_form = QuizForm()

    return render(request,
                  'quiz/create.html',
                  {'quiz_form':quiz_form,
                   'new_quiz':new_quiz})


