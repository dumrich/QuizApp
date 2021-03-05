from django.test import TestCase
from .models import Quiz, Question, SaveUserInstance
from django.contrib.auth import get_user_model


class QuizTestCase(TestCase):
    '''TestCase for the Quiz Model'''
    def setUp(self):
        """setup for Quiz TestCase"""
        user = get_user_model()
        user.objects.create_user(
            email="test",
            age=14,
            password='testpass123'
        )

    def test_create_quiz(self):
        user = get_user_model().objects.get(email='test')
        quiz = Quiz(author=user, name="test quiz", description="test description")
        quiz.save()
        self.assertEqual(quiz.name, "test quiz")

    def test_delete_quiz(self):
        """Test deletion of the quiz"""
        user = get_user_model().objects.get(email='test')
        quiz = Quiz(author=user, name="test quiz", description="test description")
        quiz.save()
        Quiz.objets.delete(name="test quiz")
        self.assertEqual(1, 1)
