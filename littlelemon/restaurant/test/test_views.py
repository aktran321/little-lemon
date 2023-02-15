from django.test import TestCase, Client
from restaurant.models import Menu
import json
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
      Menu.objects.create(title="Mohito", price=15 , inventory=100)
      Menu.objects.create(title="Taro", price=20, inventory=50)
      Menu.objects.create(title="Uni", price=25, inventory=10)
    def test_menu_model(self):
      mohito = Menu.objects.get(title="Mohito")
      self.assertEqual(mohito.price, 15)
      taro = Menu.objects.get(title="Taro")
      self.assertEqual(taro.price, 20)
      uni = Menu.objects.get(title="Uni")
      self.assertEqual(uni.price, 25)
    # ta
    def test_getall(self):
      # client is a dummy test browser, that allows you to test your views
      # allows you to simulate GET and POST requests on a URL and observe the response 
      # does not require the web server to be running
      # specify the path NOT the entire domain
      client = Client()
      response = client.get("/restaurant/menu/") # retrieve response data
      menu = Menu.objects.all() # retrieve all objects instantiated with Menu. This is the 3 instantiated objects created above.
      serializer = MenuSerializer(menu, many=True) # serialize the data
      self.assertEqual(response.data, serializer.data) # compare the expected serialized data with the response from the URL

