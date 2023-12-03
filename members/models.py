from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    OPTIONS = (
            ('Employee', 'Employee'),
            ('Manager', 'Manager'),
            ('Human Resource Officer', 'Human Resource Officer'),
            ('Temp Manager', 'Temp Manager'),
            ('Admin', 'Admin'),)
    
        
    role = models.CharField(max_length=30, choices=OPTIONS)
    
