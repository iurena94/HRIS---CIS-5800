from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["employeeid"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Error logging in, Try again ..."))
            return redirect('login') 

    else:
        return render(request, 'authenticate/login.html',{})

