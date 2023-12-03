from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, CreateUserForm
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["employeeid"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('calendar')
        else:
            messages.success(request, ("Error logging in, Try again ..."))
            return redirect('login') 

    else:
        return render(request, 'authenticate/login.html',{})

def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        # roleform = CreateUserForm(request.POST)
        if form.is_valid(): # and roleform.is_valid():
            user = form.save()
            # role = roleform.save(commit=False)
            # role.user = user
            # role.role = 'Employee'
            

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect("thankyou")
    else:
        form = RegisterUserForm()
        # roleform = CreateUserForm()
    return render(request, "authenticate/signup.html", {'form':form,}) # 'roleform':roleform})

def logout_user(request):
    logout(request)
    return redirect("home")

def adduser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        roleform = CreateUserForm(request.POST)
        if form.is_valid() and roleform.is_valid():
            user = form.save()
            role = roleform.save(commit=False)
            role.user = user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            return redirect("adduser")
    else:
        form = RegisterUserForm()
        roleform = CreateUserForm()
    return render(request, "authenticate/adduser.html", {'form':form, 'roleform':roleform})