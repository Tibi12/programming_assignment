from django.shortcuts import render
from kitchen_dashboard.models import Table, TableCart
from .models import Menu

def menu_cart(request):
    chosen_table = request.GET.get('table_number')
    table = Table.objects.get(table_number=chosen_table)
    table_carts = TableCart.objects.filter(table=table)
    print(table_carts)

    table_carts_with_total_price = [
        {'name': item.name, 'quantity': item.quantity, 'price': item.price, 'total_price': item.quantity * item.price}
        for item in table_carts
    ]
    
    total_price = sum(item['total_price'] for item in table_carts_with_total_price)

    context = {'chosen_table': chosen_table, 'table_carts': table_carts_with_total_price, 'total_price': total_price}

    return render(request, 'cart.html', context)

def menu_home(request):
    tables = Table.objects.all()
    print(tables)
    menus = Menu.objects.all()
        
    context = { 'tables': tables, 'menus': menus }
    return render(request, 'menu.html', context)