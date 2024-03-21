from urllib import request
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import login as auth_login
from bgfreshnet.accounts.forms import FreshNetUserCreationForm
from bgfreshnet.accounts.models import Profile

# Create your views here.

UserModel = get_user_model()

class LogInUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'
    success_url = reverse_lazy('index')




class FreshNetUserRegistrationView(views.CreateView):
    template_name = 'accounts/register_user.html'
    form_class = FreshNetUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result

def logout_user(request):
        logout(request)
        return redirect('index')
