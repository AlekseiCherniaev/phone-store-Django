from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class UserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}), disabled=True)
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}), disabled=True)
    image = forms.ImageField(label='Image', widget=forms.FileInput(attrs={'class': "form-input"}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'image', 'date_of_birth', 'email', 'first_name', 'last_name')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password Check', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password1': 'Password',
            'password2': 'Password Again',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-change'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-change'}))
    password2 = forms.CharField(label='Password again', widget=forms.PasswordInput(attrs={'class': 'form-change'}))

    class Meta:
        model = get_user_model()
        fields = ['old_password', 'password1', 'password2']
        labels = {
            'old_password': 'Old password',
            'password1': 'New password',
            'password2': 'Repeat the password',
        }
