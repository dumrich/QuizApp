from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('quiz:list')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        self.user = form.save(commit=False)
        self.user.save()
        new_user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password1'],
                                ) 
        login(self.request, new_user)
        return HttpResponseRedirect('/')

