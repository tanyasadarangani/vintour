from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    bio = models.TextField()

class Tour(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numberofstops = models.IntegerField()
    traveldistance = models.FloatField()
    traveltime = models.FloatField()
    regions = models.CharField(max_length=250)

class Stop(models.Model):
    Tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=50)
    hoursopen = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    
