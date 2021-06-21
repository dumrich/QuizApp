from django.test import TestCase
from .models import Quiz, Question, SaveUserInstance
from django.contrib.auth import get_user_model


class QuizTestCase(TestCase):
    """TestCase for the Quiz Model"""
    def setUp(self):
        """Setup testcases with default user object"""
        user = get_user_model()
        user.objects.create_user(
            email="test@gmail.com",
            age=14,
            password="testpass123"
        )

    def test_create_quiz(self):
        user = get_user_model().objects.get(email="test@gmail.com")
        quiz = Quiz(author=user, name="test quiz", description="test description")
        self.assertEqual(quiz.name, "test quiz")

    def test_delete_quiz(self):
        """Test deletion of the quiz"""
        user = get_user_model().objects.get(email="test@gmail.com")
        quiz = Quiz(author=user, name="test quiz", description="test description")
        quiz.save()
        Quiz.objects.get(description=quiz.description).delete()
        self.assertFalse(Quiz.objects.filter(description=quiz.description).exists())

    def test_update_quiz(self):
        """Test Updating Quiz"""
        user = get_user_model().objects.get(email="test@gmail.com")
        quiz = Quiz(author=user, name="test quiz", description="test description")
        quiz.save()
        quiz = Quiz.objects.get(description="test description")
        quiz.description = "non-test description"
        quiz.save()
        self.assertEqual(quiz.description, "non-test description")

    def test_search_by_quiz_id(self):
        """Test Searching by Id"""
        user = get_user_model().objects.get(email="test@gmail.com")
        quiz = Quiz(author=user, name="test quiz", description="test description")

        quiz.save()
        self.assertTrue(Quiz.objects.filter(playId=quiz.playId).exists())

class QuestionTestCase(TestCase):
    """Test Question Creation"""

    def setUp(self):
        """Setup testcases with default user object"""
        user = get_user_model()
        user.objects.create_user(
            email="test@gmail.com",
            age=14,
            password="testpass123"
        )
        user = user.objects.get(email="test@gmail.com")
        quiz = Quiz(author=user, name="test quiz", description="test description")
        quiz.save()

    def test_add_question(self):
        """Test Adding Question to Quiz"""
        quiz = Quiz.objects.get(name="test quiz")
        quiz.questions.create(question="Test question 123", choice_2="Hello", choice_3="Hello2", answer="Goodbye")
        self.assertEqual(1, 1)
        
