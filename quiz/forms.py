from django import forms
from .models import Quiz, Question


class QuizForm(forms.ModelForm):
    '''
    Forms for creating a quiz
    '''
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder':'Enter Name'
            }
        ))
    description = forms.CharField(widget=forms.Textarea(
        attrs = {

            'class': 'form-control',
            'id':"exampleTextarea",

            }

        ), required=False)

    class Meta:
        model=Quiz
        fields = ('name', 'description')

class QuestionForm(forms.ModelForm):
    '''
    Forms for creating a question
    '''
    question = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter question'
            }
        ))        

    class Meta:
        model=Question
        exclude = ['quiz']
