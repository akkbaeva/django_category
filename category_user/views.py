from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return User.objects.all()


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'

