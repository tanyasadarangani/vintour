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
    name = models.CharField(max_length=40, default='Newly Created Tour')
    numberofstops = models.IntegerField(blank=True)
    traveldistance = models.FloatField(blank=True)
    traveltime = models.FloatField(blank=True)
    regions = models.CharField(max_length=250)

class Stop(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=50, blank=True)
    hoursopen = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=13, blank=True)

class Winery(models.Model): 
    name = models.CharField(max_length=100)
<<<<<<< HEAD
    address = models.CharField(max_length=100, blank=True)
    desc = models.CharField(max_length=1000, blank=True)
    price = models.CharField(max_length=50, blank=True)
    rating = models.IntegerField(blank=True)
=======
    address = models.CharField(max_length=100, blank=True, default='')
    desc = models.CharField(max_length=1000, blank=True, default='')
    price = models.CharField(max_length=50, blank=True, default='')
    rating = models.CharField(max_length=10, blank=True, default='')
>>>>>>> 661d377510af71bb7abff8437496d3f42061e45d
