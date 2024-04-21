from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_home, name='menu_home'),
    path('orderitems', views.items, name='home'),
    path('cart', views.menu_cart, name='menu_cart'),
]