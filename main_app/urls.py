from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
<<<<<<< HEAD
    path('users/tour_detail/', views.tour_detail, name='tour_detail'),
=======
    path('tours/<int:tour_id>', views.tour_detail, name='tour_detail'),
>>>>>>> bdd4e70745606d04996b13ae48855bb000c123b5
    path('serp/', views.serp, name='serp'),
    path('profile/', views.profile, name='profile'),
    path('tours/add/', views.add_winery, name='add_winery'),
]