from django.shortcuts import render


def items(request):
    context = {
        'message': 'Welcome to my Django App!'
    }
    return render(request, 'orderitems.html', context)