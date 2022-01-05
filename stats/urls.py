from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking/medals/<int:year>', views.countries_by_medals, name='ranking-medals')
]
