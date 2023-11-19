from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def home(request):
    return render(request, "dashboard.html")


def thankyou(request):
    return render(request, "thankyou.html")


def logout_view(request):
    logout(request)
    return render(request, "index.html")

@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html") 

def contacts(request):
    return render(request, "")