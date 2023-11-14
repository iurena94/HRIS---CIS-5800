from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("employeeid")
        password = request.POST.get("employeeid")
        myuser = User.objects.create_user(username, password)
        myuser.save()
        return render(request,"thankyou.html")
    return render(request, "signup.html")

def thankyou(request):
    return render(request, "thankyou.html")


def logout_view(request):
    logout(request)
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html") 

def contacts(request):
    return render(request, "")