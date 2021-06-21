from django.urls import path

from .views import SignUpView, ProfileView

app_name = "users"

urlpatterns = [
        path('signup/', SignUpView.as_view(), name='signup'),
        path('profile/', ProfileView, name="profile")
]
