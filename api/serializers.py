from rest_framework import serializers
from quiz.models import Quiz, Question, UserAnswer, SaveUserInstance
from users.models import CustomUser
from quiz.models import Quiz, Question


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'age']


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ('playId', 'name', 'description', 'author')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('question', 'question_type', 'quiz',
                  'answer', 'choice_2', 'choice_3', 'choice_4')
