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
            return redirect('dashboard')
        else:
            messages.success(request, ("Error logging in, Try again ..."))
            return redirect('login') 

    else:
        return render(request, 'authenticate/login.html',{})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("employeeid")
        password = request.POST.get("employeeid")
        myuser = User.objects.create_user(username, password)
        myuser.save()
        return render(request,"thankyou.html")
    else:
        return render(request, "authenticate/signup.html")

def logout_view(request):
    logout(request)
    return redirect(request, "login")