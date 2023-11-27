from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, UserManager



# class User(models.Model):
#     username = models.CharField(max_length = 25, null = True)
#     email = models.CharField(max_length = 35, null = True)
#     password = models.CharField(max_length = 20, null = True)


#     def __str__(self):
#         return self.username


#     def get_absolute_url(self):
#         return reverse('user-detail', args=[str(self.id)])

class Chef(models.Model):
    username = models.CharField(max_length = 25, null = True)
    email = models.CharField(max_length = 35, null = True)
    password = models.CharField(max_length = 20, null = True)

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username


    def get_absolute_url(self):
        return reverse('chef-detail', args=[str(self.id)])
    

class Recipe(models.Model):
    name = models.CharField(max_length = 20, null = True)
    short_desc = models.CharField(max_length = 414, null = True)
    instruction = models.CharField(max_length = 3000, null = True)
    ingredients = models.CharField(max_length = 2000, null = True)
    chef = models.ForeignKey(Chef,  on_delete=models.CASCADE, default = None, null=True)
    recipe_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])



# Create your models here.
