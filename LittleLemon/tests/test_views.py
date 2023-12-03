from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

# Create your tests here.
class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        self.menu_item1 = Menu.objects.create(title="title1", price=10.99, inventory=50)
        self.menu_item2 = Menu.objects.create(title="title2", price=12.99, inventory=40)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)