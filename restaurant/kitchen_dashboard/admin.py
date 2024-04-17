from django.contrib import admin
from .models import Table, Order, TableCart

admin.site.register(Table)
admin.site.register(TableCart)
admin.site.register(Order)