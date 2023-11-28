from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Credential(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pw = models.CharField(max_length=200)
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'