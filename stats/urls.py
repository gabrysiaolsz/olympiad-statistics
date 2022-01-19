from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),

    # GET:
    path('athlete/ranking/by_age', views.athletes_by_age),
    path('athlete/ranking/by_medals', views.athletes_by_medals),
    path('athlete/ranking/by_weight', views.athletes_by_weight),
    path('country/ranking/by_players', views.countries_by_athletes_count),
    path('country/by_gold_medals', views.countries_by_gold_medals),
    path('country/ranking/by_medals', views.countries_by_medals),
    path('athlete/ranking/by_mean_height', views.mean_height),
    path('athlete/ranking/by_gender_ratio', views.sex_percentage),
    path('sport/ranking/by_athlete_count', views.sport_by_athlete_count),

    # templates
    path('Qby_age', views.q_athletes_by_age),
    path('Qathletes_by_medals', views.q_athletes_by_medals),
    path('Qby_weight', views.q_athletes_by_weight),
    path('Qby_players', views.q_countries_by_athletes_count),
    path('Qby_gold_medals', views.q_countries_by_gold_medals),
    path('Qcountries_by_medals', views.q_countries_by_medals),
    path('Qby_mean_height', views.q_mean_height),
    path('Qby_gender_ratio', views.q_sex_percentage),
    path('Qby_athlete_count', views.q_sport_by_athlete_count),

    # POST
    path('add_data', views.add_data),
    path('q_athlete', views.q_athlete),
    path('athlete', views.add_new_athlete),
    path('q_olympiad', views.q_olympiad),
    path('olympiad', views.add_olympiad),
    path('q_athlete_result', views.q_add_athlete_result),
    path('athlete_result', views.add_athlete_result),
    path('delete_data', views.delete_data),

    # DELETE
    path('olympiad/athlete_results', views.delete_statistics_by_id)
]
