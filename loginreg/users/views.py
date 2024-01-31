from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegistrationForm
from .models import UserProfile


class RegistrationView(CreateView):
    template_name = 'auth/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('auth:home')  # Redirect to login page upon successful registration

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        UserProfile.objects.create(user=self.object)
        return response


class AuthView(FormView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('auth:home')  # Redirect to home page upon successful login

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(FormView):
    template_name = 'auth/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('auth:home')


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'auth/profile.html'
    model = User
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user=self.request.user)
        context['user_profile'] = user_profile
        return context


class HomeView(TemplateView):
    template_name = 'auth/home.html'