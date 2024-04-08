from django.urls import path
from . import views

urlpatterns = [
    path('orderitems', views.items, name='home'),
]