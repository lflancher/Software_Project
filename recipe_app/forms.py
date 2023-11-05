from django.forms import ModelForm
from .models import *

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'short_desc')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')