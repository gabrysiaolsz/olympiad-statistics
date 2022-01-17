from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('athlete/ranking/by_age', views.athletes_by_age),
    path('athlete/ranking/by_medals', views.athletes_by_medals),
    path('athlete/ranking/by_weight', views.athletes_by_weight),
    path('country/ranking/by_players', views.countries_by_athletes_count),
    path('country/<str:country_code>/by_gold_medals', views.countries_by_gold_medals),
    path('country/ranking/by_medals/<str:medal>', views.countries_by_medals),
    path('athlete/ranking/by_mean_height', views.mean_height),
    path('athlete/ranking/by_gender_ratio', views.sex_percentage),
    path('sport/ranking/by_athlete_count', views.sport_by_athlete_count),
    
    path('olympiad/athlete_results/<int:statistics_id>', views.delete_statistics_by_id),
    path('add_data', views.add_data),
        
    path('Qby_age', views.Qathletes_by_age),
    path('Qathletes_by_medals', views.Qathletes_by_medals),
    path('Qby_weight', views.Qathletes_by_weight),
    path('Qby_players', views.Qcountries_by_athletes_count),
    path('Qby_gold_medals', views.Qcountries_by_gold_medals),
    path('Qcountries_by_medals', views.Qcountries_by_medals),
    path('Qby_mean_height', views.Qmean_height),
    path('Qby_gender_ratio', views.Qsex_percentage),
    path('Qby_athlete_count', views.Qsport_by_athlete_count)
]
