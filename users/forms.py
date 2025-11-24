from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }
        help_texts = {
            "username": "Máximo 15 caracteres.",
            "password1": "Debe tener al menos 8 caracteres, no ser común ni solo números.",
        }