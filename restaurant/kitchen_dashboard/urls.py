from django.urls import path
from . import views

urlpatterns = [
    path('place-order/<int:table_number>', views.place_order, name='place_order'),
    path('', views.kitchen_dashboard, name='kitchen_dashboard'),
    path('accept-order', views.accept_order, name='accept_order'),
    path('deliver-order', views.deliver_order, name='deliver_order'),
    path('vacate-table', views.vacate_table, name='vacate_table'),
]