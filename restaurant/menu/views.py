from django.shortcuts import render
from kitchen_dashboard.models import Table
from .models import Menu

def menu_home(request):
    tables = Table.objects.all()
    print(tables)
    menus = Menu.objects.all()

    already_selected = request.GET.get('table', None)
    if already_selected is None:
        already_selected = False
        
    context = { 'tables': tables, 'menus': menus, 'already_selected': already_selected }
    return render(request, 'menu.html', context)