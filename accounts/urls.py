# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", auth_views.LoginView.as_view(template_name='registration/signin.html'), name="signin"),
    path("signout/", auth_views.LogoutView.as_view(), name="signout")

]
