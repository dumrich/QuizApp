from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'id':'exampleInputEmail1',
            'placeholder':'Enter Email'
            }

        ))
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            'class': 'form-control'
            }
        ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'id':'exampleInputPassword1',
            'placeholder':'Password'
            }
        ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'id':'exampleInputPassword2',
            'placeholder':'Password'
            }
        ))
    class Meta:
        model = get_user_model()
        fields = ('email', 'age')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'age')
