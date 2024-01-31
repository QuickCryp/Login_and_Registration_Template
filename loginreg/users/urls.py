from django.urls import path

from .views import RegistrationView, AuthView, LogoutView, ProfileView, HomeView

app_name = 'auth'
urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('home/', HomeView.as_view(), name='home')
]