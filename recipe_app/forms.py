from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class ChefForm(ModelForm):
    class Meta:
        model = Chef
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User 
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fiels = ['url', 'name']