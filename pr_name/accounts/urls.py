from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="Login"),
    path("logout/", views.LogoutView.as_view(), name="Logout"),
    path("reset/", views.PasswordResetView.as_view(), name="reset"),
    path("change/", views.PasswordChangeView.as_view(), name="change_password"),
]