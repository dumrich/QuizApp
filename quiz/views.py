from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Quiz
from .forms import QuizForm, QuestionForm


class QuizListView(ListView):
    queryset = Quiz.objects.all()
    context_object_name = 'quizzes'
    template_name = 'quiz/list.html'

def quiz_detail(request, pk, slug):
    quiz = get_object_or_404(Quiz, pk=pk, slug=slug)
    
    questions = quiz.questions.all()

    new_question = None

    if request.method == "POST":
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            new_question = question_form.save(commit=False)
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
