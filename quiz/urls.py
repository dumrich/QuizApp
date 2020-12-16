from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    # post views
    path('', views.QuizListView.as_view(), name='quiz_list'),
    path('<int:pk>/<slug:slug>/',
         views.quiz_detail,
         name='quiz_detail'),
    path('quiz/create/',
         views.quiz_create,
         name='quiz_create'),
    path('<int:pk>/<slug:slug>/quiz/',
         views.quiz_take,
         name='quiz_take'),
    path('<int:pk>/<slug:slug>/<int:attempt>/',
         views.instance_detail,
         name="instance_detail")

 
 
]
