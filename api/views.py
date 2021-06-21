from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, generics
from users.models import CustomUser
from quiz.models import Quiz, Question
from .serializers import UserSerializer, QuizSerializer, QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def QuizDetail(request, pk):
    try:
        quiz = Quiz.objects.get(playId=pk)
    except Quiz.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
