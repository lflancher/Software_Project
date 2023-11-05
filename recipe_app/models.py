from django.db import models
from django.urls import reverse



class User(models.Model):
    username = models.CharField(max_length = 25, null = True)
    email = models.CharField(max_length = 35, null = True)
    password = models.CharField(max_length = 20, null = True)


    def __str__(self):
        return self.username


    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
    

class Recipe(models.Model):
    name = models.CharField(max_length = 20, null = True)
    short_desc = models.CharField(max_length = 414, null = True)
    instruction = models.CharField(max_length = 3000, null = True)
    ingredients = models.CharField(max_length = 2000, null = True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])



# Create your models here.
