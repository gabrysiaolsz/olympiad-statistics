from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country/ranking/by_medals/<str:medal>/<int:year>', views.countries_by_medals, name='ranking-medals'),
    path('ranking/medals/players', views.players_by_medals, name='ranking-players'),
    path('ranking/players_count/<int:year>', views.countries_by_players_count, name='ranking-players-count'),
    path('percentage/sex/<int:year>', views.sex_percentage, name='sex-percentage')
]
