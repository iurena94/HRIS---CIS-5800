from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from datetime import datetime, date, timedelta
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from .models import *
from .utils import Calendar
from .forms import EventForm
# Create your views here.

#returns current users' role
def userrole(request):
    return request.user.userprofile.role

# returns current users' id
def userid(request):
    return request.user.username  # user's username is there employee id

@login_required(login_url="login")
def home(request):
    return render(request, "calendar.html",userdetails(request))


def thankyou(request):
    return render(request, "thankyou.html")

# all events page
def allevents(request):
    my_role = userrole(request)
    id = str(userid(request))
    is_emp_or_hr = my_role in ['Employee', "Human Resource Officer"] 
    is_temp_or_manager = my_role in ["Temp Manager",'Manager'] 
    events = Event.objects.all()
    
    return render(request, "allevents.html", {'events':events, 'my_role':my_role, 'id':id, 'is_emp_or_hr':is_emp_or_hr,'is_temp_or_manager':is_temp_or_manager})

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

@login_required(login_url="login")
def allusers(request):
    user = get_user_model()
    users = user.objects.all()
    return render(request, "allusers.html",{"users":users})

def update_user_role(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        new_role = request.POST.get('new_role')
        user.userprofile.role = new_role
        user.userprofile.save()
    return redirect('allusers') 

def terminate_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return JsonResponse({'message': 'User terminated successfully'})

def update_name(request):
    if request.method == 'POST':
        new_fname = request.POST.get('newfname')
        new_lname = request.POST.get('newlname')
        user = request.user
        user.first_name = new_fname
        user.last_name = new_lname
        user.save()
    return redirect('profile')

def update_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('newemail')
        user = request.user
        user.email = new_email
        user.save()
    return redirect('profile')

def update_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        user = request.user
        user.set_password(new_password)
        user.save()
    return redirect('profile')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True, request=self.request)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    
    if request.POST and form.is_valid():
        form = form.save(commit=False)
        form.From = request.user.username
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event.html', {'form': form})