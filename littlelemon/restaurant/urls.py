#define URL route for index() view
from django.urls import path
from . import views
from .views import MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
