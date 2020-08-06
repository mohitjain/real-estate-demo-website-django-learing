from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    if request.method == "POST":
        messages.error(request, "This is a sample error")
        return redirect('register')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        print("Register")
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return redirect('index')