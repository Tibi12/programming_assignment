from django.shortcuts import render
from kitchen_dashboard.models import Table
from .models import Menu
def menu_cart(request):
    return render(request, 'cart.html')


def menu_home(request):
    tables = Table.objects.all()
    print(tables)
    menus = Menu.objects.all()
        
    context = { 'tables': tables, 'menus': menus }
    return render(request, 'menu.html', context)