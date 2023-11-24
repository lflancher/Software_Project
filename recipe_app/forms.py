from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import *

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password']