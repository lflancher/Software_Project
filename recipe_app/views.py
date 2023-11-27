from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import django.views.generic as generic
from django.views.generic import TemplateView, ListView
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import allowed_users 
from rest_framework import viewsets, permissions
from django.conf import settings

# Create your views here.


# Create your views here.


class ChefListView(generic.ListView):
   model = Chef
class ChefDetailView(generic.DetailView):
   model = Chef 
   context_object_name = "chef"


   def get_context_data(self, **kwargs):
        context = super(ChefDetailView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
class UserListView(generic.ListView):
   model = User
class UserDetailView(generic.DetailView):
   model = User 
   context_object_name = "user"


#    def get_context_data(self, **kwargs):
#         context = super(UserDetailView, self).get_context_data(**kwargs)
#         context['some_data'] = 'This is just some data'
#         return context

class RecipeListView(generic.ListView):
   model = Recipe 
class RecipeDetailView(generic.DetailView):
   model = Recipe 



def index(request):
   return render( request, 'recipe_app/index.html')

def registerPage(request):
   form = CreateUserForm()
   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         user = form.save()
         username = form.cleaned_data.get('username')
         group = Group.objects.get(name='Chef_users')
         user.groups.add(group)
         chef = Chef.objects.create(user=user, username = username)
         
         chef.save()
         messages.success(request, 'Account was created for ' + username)
         return redirect('login')

   context = {'form':form}
   return render(request, 'registration/register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Chef_users'])
def createRecipe(request):
   form = RecipeForm()
   if request.method == 'POST':
      form = RecipeForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('/')
      
   context = {'form':form}
   return render(request,'recipe_app/recipe_form.html', context)


# def createChef(request):
#    form = ChefForm()
#    if request.method == 'POST':
#       form = ChefForm(request.POST)
#       if form.is_valid():
#          form.save()
#          return redirect('/')
      
#    context = {'form':form}
#    return render(request,'recipe_app/user_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Chef_users'])
def updateRecipe(request, pk):
   recipe = Recipe.objects.get(id=pk)
   form = RecipeForm(instance = recipe)

   if request.method == 'POST':
      form = RecipeForm(request.POST, request.FILES, instance=recipe)
      if form.is_valid():
         form.save()
         return redirect('/')
      
   context = {'form':form}
   return render(request, 'recipe_app/recipe_form.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['Chef_users'])
def deleteRecipe(request, pk):
   recipe = Recipe.objects.get(id=pk)
   if request.method == "POST":
      recipe.delete()
      return redirect('/')
   context = {'item':recipe} 
   return render(request, 'recipe.app/recipe_delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Chef_users'])
def deleteChef(request, pk):
   chef = Chef.objects.get(id=pk)
   if request.method == "POST":
      chef.delete()
      return redirect('/')
   context = {'item':chef} 
   return render(request, 'recipe.app/user_delete.html', context)

   
@login_required(login_url='login')
@allowed_users(allowed_roles=['Chef_users'])
def userPage(request):
   chef = request.user.chef
   form = ChefForm(instance = chef)
   print('chef', chef)
   recipe = chef.recipe 
   print(recipe) 
   if request.method == 'POST':
      form = ChefForm(request.POST, request.FILES, instance = chef)
      if form.is_valid():
         form.save()
   context = {'recipes':recipe, 'form':form}
   return render(request, 'recipe_app/user.html', context)

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.order_by('-date_joined')
   serializer_class = UserSerializer 
   permission_classes = [permissions.IsAuthenticated if settings.ENABLE_AUTHENTICATION else permissions.AllowAny]

class GroupViewSet(viewsets.ModelViewSet):
   queryset = Group.objects.all() 
   serliazer_class = GroupSerializer 
   permission_classes = [permissions.IsAuthenticated]
   