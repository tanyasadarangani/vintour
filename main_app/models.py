from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    bio = models.TextField()

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
<<<<<<< HEAD
>>>>>>> 661d377510af71bb7abff8437496d3f42061e45d
=======

class Tour(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, default='Newly Created Tour')
    regions = models.CharField(max_length=250, blank=True)
    winery = models.ManyToManyField(Winery)    

>>>>>>> 0d94a325924b3b82ab86b3bf85886b6aad767c27
