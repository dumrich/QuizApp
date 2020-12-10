from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    # post views
    path('', views.QuizListView.as_view(), name='quiz_list'),
    
 
]
