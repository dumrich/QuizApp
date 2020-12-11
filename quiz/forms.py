from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model=Quiz
        fields = ('name', 'description',)

