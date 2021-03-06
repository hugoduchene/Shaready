from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser
from django.contrib.auth import (password_validation)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UsernameField

""" Manages registration form """


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'input_registrer', 'placeholder': 'Password'}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'input_registrer', 'placeholder': 'Confirm password'}
        ),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input_registrer', 'placeholder': 'Pseudo'}),
            'email': forms.EmailInput(attrs={'class': 'input_registrer', 'placeholder': 'Mail'}),
        }


""" Manages Change picture form """


class ChangePictureForm(forms.ModelForm):
    image_profile = forms.ImageField(
        label=('<i class="fas fa-camera"></i>'),
        widget=forms.FileInput(attrs={'class': 'import_pic', 'id': 'file'})
    )

    class Meta:
        model = CustomUser
        fields = ('image_profile',)


""" Manages user's forms """


class CustomUserForms(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input_connexion', 'placeholder': 'Pseudo'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input_connexion', 'placeholder': 'Password', 'autocomplete': 'password'}
        )
    )
