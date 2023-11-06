from django.forms import ModelForm
from .models import *

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'