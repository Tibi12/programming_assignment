from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth import login

def home(request):
    context = {
        'message': 'Welcome to my Django App!'
    }
    return render(request, 'home.html', context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home.html')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})