from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser
from django.contrib.auth import (authenticate, get_user_model, password_validation)
from django.utils.translation import gettext, gettext_lazy as _

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class' : 'input_registrer', 'placeholder' : 'Password1'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class' : 'input_registrer', 'placeholder' : 'Password2'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = { 'username' : forms.TextInput(attrs={ 'class': 'input_registrer', 'placeholder' : 'Pseudo'}),
                    'email' : forms.EmailInput(attrs={ 'class' : 'input_registrer', 'placeholder' : 'Mail'}),
                    }
        

        