from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Quiz


class QuizListView(ListView):
    queryset = Quiz.objects.all()
    context_object_name = 'quizzes'
    template_name = 'quiz/list.html'

def quiz_detail(request, pk):
    print(request)
    quiz = get_object_or_404(Quiz, pk=pk)
    
    return render(request, 
                  'blog/post/detail.html',
                  {'quiz':quiz})

