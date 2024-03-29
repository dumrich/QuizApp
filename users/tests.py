from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    '''Test Custom User Model'''
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="test@gmail.com",
            age=14,
            password="testpass123"
        )
        self.assertEqual(user.email, "test@gmail.com")
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        '''Test creation of superuser'''
        User = get_user_model()
        user = User.objects.create_superuser(
            email="test@gmail.com",
            age=14,
            password="testpass123"
        )
        self.assertEqual(user.email, "test@gmail.com")
        self.assertTrue(user.is_superuser)

    def test_update_user(self):
        '''Test Updating Superuser'''
        User = get_user_model()
        user = User.objects.create_user(
            email="test@gmail.com",
            age=14,
            password="testpass123"
        )
        user.email = "test123@yahoo.com"
        user.save()
        self.assertEqual(user.email, "test123@yahoo.com")

    def test_update_superuser(self):
        '''Test updating a superuser'''
        User = get_user_model()
        user = User.objects.create_superuser(
            email="test@gmail.com",
            age=14,
            password="testpass123"
        )
        user.email = "test123@yahoo.com"
        user.save()
        self.assertEqual(user.email, "test123@yahoo.com")
