from typing import Any
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
import django.views.generic as generic
from .models import *
from .forms import RecipeForm
from django.http import HttpResponse

# Create your views here.


# Create your views here.
class UserListView(generic.ListView):
   model = User
class UserDetailView(generic.DetailView):
   model = User 
   context_object_name = "user"
   

   def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class RecipeListView(generic.ListView):
   model = Recipe 
class RecipeDetailView(generic.DetailView):
   model = Recipe 



def index(request):

   return render( request, 'recipe_app/index.html')


def createRecipe(request):
   form = RecipeForm
   if request.method == 'POST':
      form = RecipeForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/')
      
   context = {'form':form}
   return render(request,'recipe_app/user_form.html', context)


def updateRecipe(request, pk):
   recipe = Recipe.objects.get(id=pk)
   form = RecipeForm(instance = recipe)

   if request.method == 'POST':
      form = RecipeForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/')
      
   context = {'form':form}
   return render(request, 'recipe_app/user_form.hmtl', context)

def deleteRecipe(request, pk):
   recipe = Recipe.objects.get(id=pk)
   if request.method == "POST":
      recipe.delete()
      return redirect('/')
   
   context = {'item':recipe} 
   return render(request, 'recipe.app/recipe_delete.html', context)

   