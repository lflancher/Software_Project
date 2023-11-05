from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('users/', views.UserListView.as_view(), name = 'users'),
path('user/<int:pk>', views.UserDetailView.as_view(), name = 'user-detail'),
path('recipes/', views.RecipeListView.as_view(), name = 'recipes'),
path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name = 'recipe-detail'),
path('user/<int:user_id>/create_recipe/', views.createRecipe, name='create_recipe'),

]
