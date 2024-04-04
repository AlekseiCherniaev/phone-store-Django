from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user import forms


class LoginUser(LoginView):
    form_class = forms.UserForm
    template_name = 'user/login_user.html'
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        # TO DO
        # next_url = self.request.POST.get('next')
        # if next_url:
        #     print(next_url)
        #     return next_url
        # else:
        return reverse_lazy('products')


# def register(request):
#     if request.method == 'POST':
#         form = forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1'])
#             user.save()
#             return render(request, 'user/register_done.html', {'form': form})
#     else:
#         form = forms.UserRegistrationForm()
#         return render(request, 'user/register.html', context={'form': form})


class UserRegister(CreateView):
    form_class = forms.UserRegistrationForm
    extra_context = {'title': 'Register'}
    template_name = 'user/registration_user.html'
    success_url = reverse_lazy('user:login')
