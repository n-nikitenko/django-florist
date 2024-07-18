from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """модель для пользователя для авторизации по email"""

    username = None
    email = models.EmailField(unique=True, verbose_name="email", help_text="Укажите адрес электронной почты")
    avatar = models.ImageField(upload_to="users", verbose_name="аватар", default="users/flowers.png")
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name="номер телефона")

    country = models.CharField(max_length=150, null=True, blank=True, verbose_name="страна")

    token = models.CharField(max_length=100, null=True, blank=True, verbose_name="токен")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email