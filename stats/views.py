from django.http import HttpResponse, Http404
from django.db.models import Count, Q, F
from stats.models import Statistics


def index(request):
    return HttpResponse("It's the main page")


def countries_by_medals(request, year, medal):
    if year:
        res = Statistics.objects.filter(games__year=year)
    else:
        res = Statistics.objects

    if medal == "gold":
        result = res.filter(medal__icontains='gold')
    elif medal == "silver":
        result = res.filter(medal__icontains='silver')
    else:
        result = res.filter(medal__icontains='bronze')

    result = result.values('noc__region').annotate(medals_count=Count('noc')).order_by('-medals_count')

    if not result:
        raise Http404()
    return HttpResponse(result)


def players_by_medals(request):
    result = Statistics.objects.exclude(medal__icontains='NA') \
        .values('player_id__name') \
        .annotate(gold_counts=Count('medal', filter=Q(medal__icontains='gold'))) \
        .annotate(silver_counts=Count('medal', filter=Q(medal__icontains='silver'))) \
        .annotate(bronze_counts=Count('medal', filter=Q(medal__icontains='bronze')))\
        .filter(Q(gold_counts__gte=1) | Q(silver_counts__gte=1) | Q(bronze_counts__gte=1))\
        .order_by('-gold_counts', '-silver_counts', '-bronze_counts')

    if not result:
        raise Http404()
    return HttpResponse(result)


def countries_by_players_count(request, year):
    result = Statistics.objects.filter(games__year=year)\
        .values('noc__region')\
        .annotate(players_count=Count('player_id', distinct=True))\
        .order_by('-players_count')

    if not result:
        raise Http404()
    return HttpResponse(result)


def sex_percentage(request, year):
    if year != 0:
        res = Statistics.objects.filter(games__year=year)
    else:
        res = Statistics.objects

    female_count = res.filter(player_id__sex='F').values('player_id').distinct().count()
    male_count = res.filter(player_id__sex='M').values('player_id').distinct().count()

    result = "female_percentage: " + str(round(female_count/(female_count + male_count), 3))
    result += " male_percentage: " + str(round(male_count/(female_count + male_count), 3))

    if not result:
        raise Http404()
    return HttpResponse(result)
