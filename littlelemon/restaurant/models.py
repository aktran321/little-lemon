from django.db import models

# Create your models here.
class Booking(models.Model):
  name = models.CharField(max_length = 255)
  no_of_guests = models.SmallIntegerField()
  bookingdate = models.DateField()
class Menu(models.Model):
  title = models.CharField(max_length = 255) 
  price = models.SmallIntegerField()
  inventory = models.SmallIntegerField()
