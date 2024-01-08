from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from item.models import Item
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import CustomUser, CustomUserManager

class RegisterForm(forms.ModelForm):
    email =forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'category', 'name', 'sizes', 'price', 'description', 'image')

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'category', 'name', 'sizes', 'price', 'description', 'image')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
