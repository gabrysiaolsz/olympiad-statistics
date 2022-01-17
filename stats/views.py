from django.core.exceptions import BadRequest
from django.http import Http404
from django.db.models import Count, Q, Avg
from django.shortcuts import render

from stats.models import Statistics, Athlete


def index(request):
    context = {'message': "it's the main page"}
    return render(request, 'stats/index.html', context)


def Qathletes_by_age(request):
    return render(request, 'stats/Qathletes_by_age.html')

def Qathletes_by_medals(request):
    return render(request, 'stats/Qathletes_by_medals.html')
    
def Qathletes_by_weight(request):
    return render(request, 'stats/Qathletes_by_weight.html')    
    
def Qcountries_by_athletes_count(request):
    return render(request, 'stats/Qcountries_by_athletes_count.html')       
    
def Qcountries_by_gold_medals(request):
    return render(request, 'stats/Qcountries_by_gold_medals.html')  
    
def Qcountries_by_medals(request):
    return render(request, 'stats/Qcountries_by_medals.html')  

def Qmean_height(request):
    return render(request, 'stats/Qmean_height.html')  
    
def Qsex_percentage(request):
    return render(request, 'stats/Qsex_percentage.html')  
    
def Qsport_by_athlete_count(request):
    return render(request, 'stats/Qsport_by_athlete_count.html')      
    
def add_data(request):
    return render(request, 'stats/add_data.html')  


def countries_by_medals(request, medal):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            raise BadRequest()
        res = Statistics.objects.filter(games__year=year)
    else:
        res = Statistics.objects

    if medal == "gold":
        result = res.filter(medal__icontains='gold')
    elif medal == "silver":
        result = res.filter(medal__icontains='silver')
    elif medal == "bronze":
        result = res.filter(medal__icontains='bronze')
    else:
        raise BadRequest()

    result = result.values('country_code__country_name') \
        .annotate(medals_count=Count('country_code')) \
        .order_by('-medals_count')

    if not result:
        raise Http404()

    context = {'res': result}
    return render(request, 'stats/countries_by_medals.html', context)


def athletes_by_medals(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            raise BadRequest()
        result = Statistics.objects.filter(games__year=year)
    else:
        result = Statistics.objects

    result = result.exclude(medal__icontains='NA') \
        .values('player_id__name') \
        .annotate(gold_counts=Count('medal', filter=Q(medal__icontains='gold'))) \
        .annotate(silver_counts=Count('medal', filter=Q(medal__icontains='silver'))) \
        .annotate(bronze_counts=Count('medal', filter=Q(medal__icontains='bronze'))) \
        .filter(Q(gold_counts__gte=1) | Q(silver_counts__gte=1) | Q(bronze_counts__gte=1)) \
        .order_by('-gold_counts', '-silver_counts', '-bronze_counts')

    if not result:
        raise Http404()

    context = {'res': result, 'year': year}
    return render(request, 'stats/athletes_by_medals.html', context)


def countries_by_athletes_count(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            raise BadRequest()
        result = Statistics.objects.filter(games__year=year)
    else:
        result = Statistics.objects

    result = result.values('country_code__country_name') \
        .annotate(athlete_count=Count('player_id', distinct=True)) \
        .order_by('-athlete_count')

    if not result:
        raise Http404()

    context = {'res': result, 'year': year}
    return render(request, 'stats/countries_by_athletes_count.html', context)


def sex_percentage(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
            result = "year: " + str(year)
        except:
            raise BadRequest()
        res = Statistics.objects.filter(games__year=year)
    else:
        res = Statistics.objects
        result = "whole olympiad, "

    female_count = res.filter(player_id__sex='F').values('player_id').distinct().count()
    male_count = res.filter(player_id__sex='M').values('player_id').distinct().count()

    #result += "female_percentage: " + str(round(female_count / (female_count + male_count), 3))
    #result += " male_percentage: " + str(round(male_count / (female_count + male_count), 3))

    if not result:
        raise Http404()

    context = {'female': round(female_count / (female_count + male_count), 3), 
               'male': round(male_count / (female_count + male_count), 3), 
               'year': year}
    return render(request, 'stats/sex_percentage.html', context)


def sport_by_athlete_count(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            raise BadRequest()
        result = Statistics.objects.filter(games__year=year)
    else:
        result = Statistics.objects

    result = result.values('player_id__statistics__sport') \
        .annotate(athlete_count=Count('player_id', distinct=True)) \
        .order_by('-athlete_count')

    if not result:
        raise Http404()

    context = {'res': result, 'year': year}
    return render(request, 'stats/sport_by_athlete_count.html', context)


def athletes_by_weight(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            raise BadRequest()
        result = Statistics.objects.filter(games__year=year)
    else:
        result = Statistics.objects

    result = result.values('player_id__name', 'weight').order_by('-weight').distinct()

    if not result:
        raise Http404()

    context = {'res': result, 'year': year}
    return render(request, 'stats/athletes_by_weight.html', context)


def athletes_by_age(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            raise BadRequest()
        result = Statistics.objects.filter(games__year=year)
    else:
        result = Statistics.objects

    result = result.exclude(age=-1).values('player_id__name', 'age').order_by('-age').distinct()

    if not result:
        raise Http404()

    context = {'res': result, 'year': year}
    return render(request, 'stats/athletes_by_age.html', context)


def countries_by_gold_medals(request, country_code):

    result = Statistics.objects.filter(country_code__country_code__icontains=country_code)\
        .filter(medal__icontains='gold')\
        .values('games_id').annotate(medal_count=Count('games_id'))\
        .order_by('-medal_count')

    if not result:
        raise Http404()

    context = {'res': result}
    return render(request, 'stats/countries_by_gold_medals.html', context)


def delete_statistics_by_id(request, statistics_id):
    try:
        record = Statistics.objects.get(pk=statistics_id)
        record.delete()
    except:
        raise Http404("delete unsuccessful")

    context = {'res': "delete successful"}
    return render(request, 'stats/delete_statistics_by_id.html', context)


def mean_height(request):

    f = Athlete.objects.filter(sex__exact='F').aggregate(Avg('height'))
    m = Athlete.objects.filter(sex__exact='M').aggregate(Avg('height'))

    if not f or not m:
        raise Http404()

    context = {'female_mean': f, 'male_mean': m}
    return render(request, 'stats/mean_height.html', context)
