from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include, reverse_lazy

from user import views

app_name = 'user'

urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('register/', views.UserRegister.as_view(), name='register'),

    path('add-to-basket/', views.add_to_basket, name='add_to_basket'),
    path('delete-from-basket/<int:product_id>/', views.delete_from_basket, name='delete_from_basket'),

    path('password-reset/',
         PasswordResetView.as_view(
             template_name='user/password_reset_form.html',
             email_template_name='user/password_reset_email.html',
             success_url=reverse_lazy('user:password_reset_done')
         ),
         name='password_reset'),

    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html',
             success_url=reverse_lazy('user:password_reset_complete')
         ),
         name='password_reset_confirm'),

    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),
]
