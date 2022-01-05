from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking/medals/<int:year>/<str:medal>', views.countries_by_medals, name='ranking-medals'),
    path('ranking/medals/players', views.players_by_medals, name='ranking-players')
]
