from django.urls import path, re_path as url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("thankyou/", views.thankyou, name="thankyou"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]