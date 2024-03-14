from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    profile_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    calendar = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.username
    
class Lead(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
