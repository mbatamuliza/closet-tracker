from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ClothingItem


class ClothingItemForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields =['name','category', 'color', 'size', 'image', 'notes']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    