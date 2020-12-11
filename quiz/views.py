from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Quiz
from .forms import QuizForm


class QuizListView(ListView):
    queryset = Quiz.objects.all()
    context_object_name = 'quizzes'
    template_name = 'quiz/list.html'

def quiz_detail(request, pk, slug):
    quiz = get_object_or_404(Quiz, pk=pk, slug=slug)
    
    return render(request, 
                  'quiz/detail.html',
                  {'quiz':quiz})

#def quiz_create(request):
#    if request.method == 'POST':
#        QuizForm = QuizForm(data=request.POST)
#        if QuizForm.is_valid():
#            new_quiz = QuizForm.save()

