from django import forms
from .models import RegisteredForms


class FormRegisterForm(forms.ModelForm):
    class Meta:
        model= RegisteredForms
        fields= ["username", "email", "phone_number", "password",]