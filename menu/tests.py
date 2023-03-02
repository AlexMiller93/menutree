from django.test import TestCase
from django.urls import reverse

from .models import Menu

# Create your tests here.
class MenuTests(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            title="Test Menu", slug="test_menu",
            named_url = "")
    
    def test_string_representation(self):
        menu = Menu(title='Main page')
        self.assertEqual(str(menu), menu.title)
    
    def test_get_absolute_path(self):
        self.assertEqual(self.menu.get_absolute_path(), '/test_menu/')

    def test_menu_attributes(self):
        self.assertEqual(f'{self.menu.title}', 'Test Menu')
        self.assertEqual(f'{self.menu.slug}', 'test_menu')
        self.assertEqual(f'{self.menu.named_url}', '')
        
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

