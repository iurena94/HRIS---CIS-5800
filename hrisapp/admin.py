from django.contrib import admin
from .models import Event, Request, Feedback

# Register your models here.
admin.site.register(Event)
admin.site.register(Request)
admin.site.register(Feedback)