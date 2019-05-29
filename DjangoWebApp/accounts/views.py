from django.views.generic import CreateView
from .models import Actor


class UserCreateView(CreateView):
    model = Actor
    template_name = 'login.html'
    fields = ('name', 'email', 'password')
