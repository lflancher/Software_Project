from django.test import TestCase, SimpleTestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User 
from recipe_app.models import Recipe, Chef
from django.urls import reverse
import time



class Hosttest(LiveServerTestCase):
    

    def testhomepage(self):
        #driver = webdriver.Chrome()
        driver = webdriver.Edge(executable_path = r"C:\Users\lflan\Documents\Software_Project\recipe_app\msedgedriver.exe")

        driver.get('http://127.0.0.1:8000/')
        
        assert "Hello, world!" in driver.title

 class LoginFormTest(LiveServerTestCase):

     def testform(self):
         driver = webdriver.Edge(executable_path = r"C:\Users\lflan\Documents\Software_Project\recipe_app\msedgedriver.exe")
         driver.get('http://127.0.0.1:8000/accounts/login/?next=/')

         time.sleep(3)

         user_name = driver.find_element_by_id('id_username')
         user_password = driver.find_element_by_id('id_password')

         time.sleep(3)

         submit = driver.find_element_by_name('submit')

         user_name.send_keys('s_username')
         user_password.send_keys('s_password')

         submit.send_keys(Keys.RETURN)

         assert 's_username' in driver.page_source

     class ViewRecipesTest(LiveServerTestCase):
         driver = webdriver.Edge(executable_path = r"C:\Users\lflan\Documents\Software_Project\recipe_app\msedgedriver.exe")
         driver.get('http://127.0.0.1:8000/')

       

         recipe_list = driver.find_element("xpath", "//a[@title= 'Browse our List of Recipes']")

         recipe_list.click()



class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class RecipeModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.recipe = Recipe.objects.createRecipe(name = 'Test Recipe')
        self.chef = Chef.objects.createChef(username='Ness')

    def test_recipe_str(self):
        self.assertEqual(str(self.post), 'Test Recipe')

    def chef_recipe_str(self):
        self.assertEqual(str(self.post), 'Ness')


# Create your tests here.
