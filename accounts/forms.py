from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="ID")
    nickname = forms.CharField(label="Nickname")
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label=("Password 재입력"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "nickname")

class CustomUsernameField(UsernameField):
    default_error_messages = {
        "required": ("ID를 입력하세요."),
    }

class CustomCharField(forms.CharField):
    default_error_messages = {
        "required": ("Password를 입력하세요."),
    }

class LoginForm(AuthenticationForm):
    username = CustomUsernameField(widget=forms.TextInput(attrs={"autofocus": True}), label='ID')
    password = CustomCharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    error_messages = {
        "invalid_login": (
            "ID 또는 Password가 틀렸습니다."
        ),
        "inactive": ("This account is inactive."),
    }
