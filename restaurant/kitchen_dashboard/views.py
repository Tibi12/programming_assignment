from django.shortcuts import render, redirect
from .models import Table, Order

def kitchen_dashboard(request):
    orders = Order.objects.filter(order_type="active").order_by('table')  

    free_table_flags = {}
    free_tables = {}
    
    for item in orders:
        free_table_flags[item.table.table_number] = {
            'pending': 0,
            'cooking': 0,
            'completed': 0,
            'total': 0
        }
    
    for item in orders:
        free_table_flags[item.table.table_number][item.status] += 1
        free_table_flags[item.table.table_number]['total'] += 1    
        
        if free_table_flags[item.table.table_number]['total'] == free_table_flags[item.table.table_number]['completed']:
            free_tables[item.table.table_number] = True
        else:
            free_tables[item.table.table_number] = False
                        
    for order in orders:
        if free_tables[order.table.table_number] == True:
            order.vacate = True
        
    context = {'orders': orders, 'free_tables': free_tables}
        
    return render(request, 'dashboard.html', context)
    
def accept_order(request):
    order_id = request.POST.get('order_id')
    order = Order.objects.get(pk=order_id)
    order.status = "cooking"
    order.save()
    
    return redirect('kitchen_dashboard')

def deliver_order(request):
    order_id = request.POST.get('order_id')
    order = Order.objects.get(pk=order_id)
    order.status = "completed"
    order.save()
    
    return redirect('kitchen_dashboard')


def vacate_table(request):
    table_number = request.POST.get('table_number')

    table = Table.objects.get(table_number=table_number)
    orders = Order.objects.filter(table=table)
    
    for item in orders:
        item.order_type = "inactive"
        item.save()
    
    table.status = "free"
    table.save()
    
    return redirect('kitchen_dashboard')