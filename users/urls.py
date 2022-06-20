from django.urls import path
from users.api import viewsets

urlpatterns = [
    path("login/", viewsets.AuthLoginView.as_view()),
    path("logout/", viewsets.AuthLogOutView.as_view()),
]
