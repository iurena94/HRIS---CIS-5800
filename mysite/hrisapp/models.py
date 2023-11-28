from django.db import models
from django.contrib.auth.models import User

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
    title = models.CharField(max_length=200, default=" ", editable=False)
    description = models.TextField(max_length=600, default=" ", editable=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()