from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class ApiTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create a User"""
        testuser1 = get_user_model().objects.create_user(
            email="testuser1", password="abc123")
        testuser1.save()
