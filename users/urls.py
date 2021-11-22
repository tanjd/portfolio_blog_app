from django.urls import path
from .views import UserRegisterView, profile

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("profile/", profile, name="profile"),
]
