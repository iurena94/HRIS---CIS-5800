from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def thankyou(request):
    return render(request, "thankyou.html")

def login(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html") 