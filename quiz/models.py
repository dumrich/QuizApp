from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.template.defaultfilters import slugify
import random
import string


def key_generator():
    '''Generate random playId for Quiz'''
    key = '1'+''.join(random.choice(string.digits) for x in range(6))
    if Quiz.objects.filter(playId=key).exists():
        key = key_generator()
    return key


class Quiz(models.Model):
    '''
    Database model for quiz
    '''
    playId = models.CharField(
        max_length=7, editable=False, default=key_generator)
    name = models.CharField(max_length=80)
    slug = models.SlugField(null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Quiz, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('quiz:quiz_detail',
                       args=[self.playId,
                             self.slug])


class Question(models.Model):
    '''
    Database Table for question
    '''
    TYPE_CHOICES = (
        ('MC', 'Multiple Choice'),
        ('TF', 'True False'),
        ('T', 'Type Answer'),
        ('D', 'Dropdown'),
    )
    question = models.CharField(max_length=254)
    question_type = models.CharField(max_length=10,
                                     choices=TYPE_CHOICES)

    quiz = models.ForeignKey(Quiz,
                             on_delete=models.CASCADE,
                             related_name='questions')

    answer = models.CharField(max_length=254)
    choice_2 = models.CharField(max_length=250, null=True)
    choice_3 = models.CharField(max_length=254, null=True)
    choice_4 = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.question


class UserAnswer(models.Model):
    '''
    Database table for User Answer
    '''
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='user'
                             )
    quiz = models.ForeignKey(Quiz,
                             on_delete=models.CASCADE)

    answer = models.CharField(max_length=255)
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE
                                 )

    def __str__(self):
        return self.answer


class SaveUserInstance(models.Model):
    '''
    Database table for User Instance
    '''
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE
                             )
    quiz = models.ForeignKey(Quiz,
                             on_delete=models.CASCADE)
    attempt = models.IntegerField(default=0)

    UserAnswer = models.ManyToManyField(UserAnswer,
                                        related_name='answers')
    score = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('quiz:insatnce_detail',
                       args=[self.quiz.id,
                             self.quiz.slug,
                             self.attempt])
