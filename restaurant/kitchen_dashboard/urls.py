from django.urls import path
from . import views

urlpatterns = [
    path('', views.kitchen_dashboard, name='kitchen_dashboard')
]