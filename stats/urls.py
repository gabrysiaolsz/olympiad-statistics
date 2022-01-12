from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('country/ranking/by_medals/<str:medal>', views.countries_by_medals),
    path('athlete/ranking/by_medals', views.athletes_by_medals),
    path('country/ranking/by_players', views.countries_by_athletes_count),
    path('athlete/ranking/by_gender_ratio', views.sex_percentage),
    path('sport/ranking/by_athlete_count', views.sport_by_athlete_count),
    path('athlete/ranking/by_weight', views.athletes_by_weight)
]
