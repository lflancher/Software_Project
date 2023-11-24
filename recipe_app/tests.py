from django.test import TestCase
from django.contrib.auth.models import User 
from recipe_app.models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='deb', password='finaliter')
        self.recipe = Recipe.objects.createRecipe(name='fish')


    def test_post_str(self):
        self.assertEqual(str(self.recipe), 'fish')

# Create your tests here.
