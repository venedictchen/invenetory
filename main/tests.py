from django.test import TestCase, Client
from .models import Item
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
        
    def test_model_creation(self):
        item = Item.objects.create(name='Test Name',amount=0,description='Test Description',code=0,price=0)
        self.assertEqual(item.name, 'Test Name')
        self.assertEqual(item.amount, 0)
        self.assertEqual(item.description, 'Test Description')