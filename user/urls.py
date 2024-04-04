from django.contrib.auth.views import LogoutView
from django.urls import path, include

from user import views

app_name = 'user'

urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', views.UserRegister.as_view(), name='register'),
]