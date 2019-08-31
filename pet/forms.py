from django import forms
from django.contrib.auth.models import User

from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ["available"]

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = "__all__"

