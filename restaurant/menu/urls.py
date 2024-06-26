from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_home, name='menu_home'),
    path('cart', views.menu_cart, name='menu_cart'),
    path('menu-orders', views.menu_orders, name='menu_orders'),
    path('menu-cart', views.add_to_menu_cart, name='add_to_menu_cart'),
]