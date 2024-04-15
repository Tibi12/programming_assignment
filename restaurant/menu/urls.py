from django.urls import path
from . import views

urlpatterns = [
    path('orderitems', views.items, name='home'),
    path('cart', views.menu_cart, name='menu_cart'),
]