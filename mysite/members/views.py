from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["employeeid"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("Error logging in, Try again ..."))
            return redirect('login') 

    else:
        return render(request, 'authenticate/login.html',{})

def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect("thankyou")
    else:
        form = RegisterUserForm()
    return render(request, "authenticate/signup.html", {'form':form})

def logout_user(request):
    logout(request)
    return redirect("home")