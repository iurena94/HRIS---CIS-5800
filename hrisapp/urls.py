from django.urls import path, re_path as url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("thankyou/", views.thankyou, name="thankyou"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path("allusers/", views.allusers, name="allusers"),
    path('terminate_user/<int:user_id>/', views.terminate_user, name='terminate_user'),
    path('update_user_role/<int:user_id>/', views.update_user_role, name='update_user_role'),
    path('update_name/', views.update_name, name='update_name'),
    path('update_email/', views.update_email, name='update_email'),
    path('update_password/', views.update_password, name='update_password'),
    path('allevents',views.allevents, name='allevents'),

]