from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from googleplaces import GooglePlaces, types, lang
import os
from .models import Winery, Tour, User
from django.db.models import Q

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def tour_detail(request, tour_id):
    map_key = os.environ['MAP_KEY']
    # Get tour
    tour = Tour.objects.get(id=tour_id)
    # Set tour start and finish
    origin = tour.winery.all().first().name
    destination = tour.winery.all().last().name
    # List all wineries in tour except start and finish
    waypoint_list = list(tour.winery.all().values('name'))
    waypoints = list(tour.winery.all().exclude(Q(name=origin) | Q(name=destination)).values('name'))
    # Replace list dicts with 
    for idx, waypoint in enumerate(waypoint_list):
      waypoint_list[idx] = waypoint['name']
    for idx, waypoint in enumerate(waypoints):
      waypoints[idx] = waypoint['name'].replace(' ', '+')
    for idx, waypoint in enumerate(waypoints):
      waypoints[idx] = waypoints[idx].replace('.', '')
    for idx in range(len(waypoints) - 1):
      waypoints[idx] = waypoints[idx] + '|'

    waypoint_concat = ''.join(waypoints)


    embed_url = f'https://www.google.com/maps/embed/v1/directions?key={ map_key }&origin={ origin }&destination={ destination }&waypoints={ waypoint_concat }' 

    return render(request, 'tour_detail.html', {
      'map_key': map_key,
      'tour': tour,
      'embed_url': embed_url,
      'waypoint_list': waypoint_list,
      'waypoint_concat': waypoint_concat
      })

def serp(request):
  key = os.environ['MAP_KEY']
  #google_places = GooglePlaces(key)
  #query_result = google_places.nearby_search(location='Napa, California', keyword='Winery')

  if request.user.is_authenticated:
    tours = Tour.objects.filter(user=request.user.id)    
  else:
    tours = None

  query_result = Winery.objects.all()

  return render(request, 'serp.html', {'key': key, 'query_result': query_result, 'tours': tours})