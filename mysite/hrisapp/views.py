from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("employeeid")
        password = "ps123"
        myuser = User.objects.create_user(username, password)
        myuser.save()
        return redirect("thankyou.html")
    return render(request, "signup.html")

def thankyou(request):
    return render(request, "thankyou.html")

def login(request):
    if request.method == 'POST':
        usern = request.POST.get("employeeid")
        pw = request.POST.get("password")
        user = authenticate(username=usern, password=pw)
        if user is not None:
            login(request, user)
            fname = usern
            return render(request, "dashboard.html", {'fname':fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect("login")
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html") 

def contacts(request):
    return render(request, "")