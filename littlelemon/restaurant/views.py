from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serialzier_class = MenuSerializer
class BookingViewset(viewsets.ModelViewSet): # model viewsets automatically handles CRUD operations
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [permissions.IsAuthenticated] # only authenticated users can access the bookings