from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def home(request):
    context = {
        'message': 'Welcome to my Django App!'
    }
    return render(request, 'home.html', context)

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('kitchen_dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_login')
        else:
            print("error")
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})