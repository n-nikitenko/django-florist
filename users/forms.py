from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from catalog.forms import StyleFormMixin
from users.models import User


class RegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя по email и паролю"""
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
