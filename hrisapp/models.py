from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    From = models.CharField(max_length=30, blank=False, default='Admin', editable=False)
    receiver = models.CharField(max_length=200, default='ALL')
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def get_url(self):
        url = reverse('event_edit', args=(self.id,))
        return url

class Request(models.Model):
    OPTIONS = (
            ('Manager', 'Manager'),
            ('Human Resources', 'Human Resources'),)
    TOPIC_OPTIONS= (
            ('Schedule Change', 'Schedule Change'),
            ('Availability', 'Availability'),
            ('Request Meeting', 'Request Meeting'),)
    sendto = models.CharField(max_length=30, choices=OPTIONS)
    From = models.CharField(max_length=30, blank=False, editable=False)
    topic = models.CharField(max_length=30, choices=TOPIC_OPTIONS)
    content = models.TextField()
