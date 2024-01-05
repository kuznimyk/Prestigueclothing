from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from item.models import Item

class RegisterForm(UserCreationForm):
    email =forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'category', 'name', 'sizes', 'price', 'description', 'image')

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'category', 'name', 'sizes', 'price', 'description', 'image')

