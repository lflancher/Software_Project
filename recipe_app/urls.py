from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet) 
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
# path('', views.index, name='index'),
# path('users/', views.UserListView.as_view(), name = 'users'),
# path('acccounts/', include('django.contrib.auth.urls')),
# path('user/<int:pk>', views.UserDetailView.as_view(), name = 'user-detail'),
# path('recipes/', views.RecipeListView.as_view(), name = 'recipes'),
# path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name = 'recipe-detail'),
# path('create_recipe/', views.createRecipe, name='create_recipe'),
# path('create_user/', views.createUser, name='create_user'),
# path('update_recipe/<str:pk>/', views.updateRecipe, name = 'update_recipe'),
# path('delete_recipe/<str:pk>/', views.deleteRecipe, name = 'delete_recipe'),
# path('delete_user/<str:pk>/', views.deleteUser, name = 'delete_user'),
# path('search/',  SearchResultsView.as_view(), name = 'search_results')
path('', views.index, name='index'),
path('chefs/', views.ChefListView.as_view(), name = 'chefs'),
path('chef/<int:pk>', views.ChefDetailView.as_view(), name = 'chef-detail'),
path('recipes/', views.RecipeListView.as_view(), name = 'recipes'),
path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name = 'recipe-detail'),
path('create_recipe/', views.createRecipe, name='create_recipe'),
path('update_recipe/<str:pk>/', views.updateRecipe, name = 'update_recipe'),
path('delete_recipe/<str:pk>/', views.deleteRecipe, name = 'delete_recipe'),
path('user/', views.userPage, name = 'user_page'),
path('account/register/', views.registerPage, name= 'register_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
