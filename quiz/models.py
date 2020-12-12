from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.template.defaultfilters import slugify

class Quiz(models.Model):
    '''
    Database model for quiz
    '''
    name = models.CharField(max_length=80)
    slug = models.SlugField(null=True)
    description = models.TextField()
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
                       args=[self.id,
                             self.slug])


class Question(models.Model):
    '''
    Database Table for question
    '''
    TYPE_CHOICES = (
            ('MC', 'Multiple Choice'),
            ('TF', 'True False'),
            ('M', 'Matching'),
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
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE
                             )
    quiz = models.ForeignKey(Quiz,
                             on_delete=models.CASCADE)
    attempt = models.IntegerField(default=0)
    
    UserAnswer = models.ManyToManyField(UserAnswer,
                                        related_name='answers')

    def __str__(self):
        return self.user.email
