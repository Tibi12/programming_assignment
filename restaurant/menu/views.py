from django.shortcuts import render


def items(request):
    context = {
        'message': 'Welcome to my Django App!'
    }
    return render(request, 'orderitems.html', context)


def menu_home(request):
    menus = Menu.objects.all()
        
    context = { 'menus': menus }
    return render(request, 'menu.html', context)