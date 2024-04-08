from django.shortcuts import render

def home(request):
    context = {
        'message': 'Welcome to my Django App!'
    }
    return render(request, 'home.html', context)