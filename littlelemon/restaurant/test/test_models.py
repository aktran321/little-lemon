from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        # create a Menu Item using .create() method
        item = Menu.objects.create(title="IceCream", price=5, inventory=100) 
        # create a variable of what we expect to be created from the model Menu that we are using create() on
        expected_item = {"title": "IceCream", "price": 5}
        # specify what you are looking for using self.assertEqual
        self.assertEqual(item.title, expected_item["title"])
        self.assertEqual(item.price, expected_item["price"])
