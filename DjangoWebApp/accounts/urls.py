from django.urls import path

from .views import UserCreateView
urlpatterns = [
    path('login', UserCreateView.as_view()),
]