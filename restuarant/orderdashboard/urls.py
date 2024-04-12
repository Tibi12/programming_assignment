from django.urls import path
from . import views

urlpatterns = [
    path('orderdashboard', views.items, name='orderdashboard'),
]
