from django.db import models


class NocRegions(models.Model):
    noc = models.CharField(primary_key=True, max_length=4)
    region = models.CharField(max_length=50)


class OlympiadInfo(models.Model):
    games = models.CharField(max_length=15, unique=True)
    year = models.IntegerField()
    season = models.CharField(max_length=10)
    city = models.CharField(max_length=30)


class Player(models.Model):
    name = models.CharField(max_length=120)
    height = models.CharField(max_length=5)
    sex = models.CharField(max_length=1)


class Statistics(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    age = models.CharField(max_length=5)
    weight = models.CharField(max_length=20)
    noc = models.ForeignKey(NocRegions, on_delete=models.CASCADE)
    games = models.ForeignKey(OlympiadInfo, to_field="games", on_delete=models.CASCADE)
    sport = models.CharField(max_length=25)
    event = models.CharField(max_length=90)
    medal = models.CharField(max_length=10)
