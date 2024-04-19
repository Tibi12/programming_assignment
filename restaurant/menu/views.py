from django.shortcuts import render
from kitchen_dashboard.models import Table, TableCart
from .models import Menu

def menu_cart(request):
    chosen_table = request.GET.get('table_number')
    table = Table.objects.get(table_number=chosen_table)
    table_carts = TableCart.objects.filter(table=table)
    print(table_carts)

    return render(request, 'cart.html')

def menu_home(request):
    tables = Table.objects.all()
    print(tables)
    menus = Menu.objects.all()
        
    context = { 'tables': tables, 'menus': menus }
    return render(request, 'menu.html', context)