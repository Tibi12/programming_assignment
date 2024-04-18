from django.shortcuts import render, redirect
from .models import Order

def kitchen_dashboard(request):
    orders = Order.objects.filter(order_type="active").order_by('table')  
        
    context = {'orders': orders}
        
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