from django.shortcuts import render, redirect
from django.urls import reverse
from kitchen_dashboard.models import Table, TableCart, Order
from .models import Menu

def menu_home(request):
    tables = Table.objects.all()
    menus = Menu.objects.all()
    
    already_selected = request.GET.get('table', None)
    if already_selected is None:
        already_selected = False
        
    context = {'tables': tables, 'menus': menus, 'already_selected': already_selected }
    return render(request, 'menu.html', context)

def menu_cart(request):
    chosen_table = request.GET.get('table_number')
    table = Table.objects.get(table_number=chosen_table)
    table_carts = TableCart.objects.filter(table=table)
    
    table_carts_with_total_price = [
        {'name': item.name, 'quantity': item.quantity, 'price': item.price, 'total_price': item.quantity * item.price}
        for item in table_carts
    ]
    
    total_price = sum(item['total_price'] for item in table_carts_with_total_price)
    
    context = {'chosen_table': chosen_table, 'table_carts': table_carts_with_total_price, 'total_price': total_price}
    return render(request, 'cart.html', context)

def menu_orders(request):
    chosen_table = request.GET.get('table_number')
    table = Table.objects.get(table_number=chosen_table)
    orders = Order.objects.filter(table=table, order_type="active")
    context = {'chosen_table': chosen_table, 'orders': orders}
    return render(request, 'menu_orders.html', context)

def add_to_menu_cart(request):
    if request.method == 'POST':
        menu_id = request.POST.get('menu_id')
        table_number = request.POST.get('table_number')
        request.session['selected_table'] = table_number
        
        menu = None
        table = Table.objects.get(table_number=table_number)
        try:
            menu = Menu.objects.get(pk=menu_id)
        except Menu.DoesNotExist:
            return redirect('menu_home')
        
        try:
            table_cart_item = TableCart.objects.get(table=table, menu_item=menu)
            table_cart_item.quantity += 1
        except TableCart.DoesNotExist:
            table_cart_item = TableCart.objects.create(
                table=table,
                menu_item=menu,
                name=menu.name,
                quantity=1,
                price=menu.price
            )
        table_cart_item.save()
            
        return redirect(reverse('menu_home') + '?table='+str(table_number))