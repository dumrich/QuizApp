from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Quiz


class QuizListView(ListView):
    queryset = Quiz.objects.all()
    context_object_name = 'quizzes'
    template_name = 'quiz/list.html'

