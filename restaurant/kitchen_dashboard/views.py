from django.shortcuts import render

def kitchen_dashboard(request):
    orders = Order.objects.filter(order_type="active").order_by('table')  
        
    context = {'orders': orders}
        
    return render(request, 'dashboard.html', context)
