from django.urls import include, path
from rest_framework import routers
from .views import QuizList, QuizDetail, QuestionList, QuestionDetail
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', csrf_exempt(QuizDetail)),
    path('list/', csrf_exempt(QuizList.as_view())),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('question/', QuestionList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
]
