from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from quiz.models import Quiz, SaveUserInstance
from django.contrib.auth.decorators import login_required
from django.db.models import Avg


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


@login_required
def ProfileView(request):
    user_quizzes = SaveUserInstance.objects.filter(user=request.user)
    print(user_quizzes)
    quiz_list = list({instance.quiz for instance in user_quizzes})
    average_quizzes = []
    total_questions = []
    for name in quiz_list:
        print(user_quizzes.filter(quiz=name).aggregate(Avg('score')))
        average_quizzes.append(str(round(user_quizzes.filter(quiz=name).aggregate(Avg('score'))['score__avg'], 2)))
    print(average_quizzes)
    print(quiz_list)
    context_dictionary = {
        "quiz-count": len(user_quizzes), "quizzes": zip(quiz_list, average_quizzes)}
    return render(request, "users/profile.html", context_dictionary)
