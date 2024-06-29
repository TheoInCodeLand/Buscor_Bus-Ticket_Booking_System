# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')
        else:
            print(form.errors)  # Debug: Print form errors if not valid
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    return render(request, 'signin.html')

def success(request):
    return render(request, 'success.html')

def dashboard(request):
    return render(request, 'dashboard.html')
