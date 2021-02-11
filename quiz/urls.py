from django.urls import path
from . import views
from .views import quiz_render_pdf_view

app_name = 'quiz'

# These are URL definitions for quiz views 
urlpatterns = [
    # quiz views

    #list all quizzes
    path('', views.QuizListView.as_view(), name='quiz_list'),

    #view quiz in depth
    path('<int:pk>/<slug:slug>/',
         views.quiz_detail,
         name='quiz_detail'),

    #create a quiz
    path('quiz/create/',
         views.quiz_create,
         name='quiz_create'),

    #take a quiz
    path('<int:pk>/<slug:slug>/quiz/',
         views.quiz_take,
         name='quiz_take'),

    #View Quiz detail
    path('<int:pk>/<slug:slug>/<int:attempt>/',
         views.instance_detail,
         name="instance_detail"),

    #view quiz pdf
    path('pdf/<pk>', quiz_render_pdf_view, name='pdf-view'),

    # Delete Quiz View
    path('<int:pk>/<slug:slug>/delete/', views.quiz_delete, name="quiz_delete")

 
 
]
