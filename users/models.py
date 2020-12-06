from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, age=None):
        if not email:
            raise ValueError('Please set the email')
        email = self.normalize_email(email)
        user = self.model(email=email.lower(), age=age)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, age):
        user = self.create_user(email, password, age=age)
        user.is_staff = True
        user.is_superuser = True
        user.save()

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=256, unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['age']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-created"]
