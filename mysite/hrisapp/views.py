from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, date
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar
# Create your views here.

@login_required(login_url="login")
def home(request):
    return render(request, "calendar.html",userdetails(request))


def thankyou(request):
    return render(request, "thankyou.html")


def logout_view(request):
    logout(request)
    return render(request, "index.html")

@login_required(login_url="login")
def dashboard(request):
    return render(request, "calendar.html",userdetails(request)) 

@login_required(login_url="login")
def profile(request):
    return render(request,"profile.html", userdetails(request))

def contacts(request):
    return render(request, "")

def userdetails(request):
    id = request.user.username
    fname = request.user.first_name
    lname = request.user.last_name
    email = request.user.email
    return {"id":id,"fname":fname,"lname":lname,'email':email}

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()