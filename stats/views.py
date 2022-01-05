from django.http import HttpResponse, Http404
from django.db.models import Count, Q, F
from stats.models import Statistics


def index(request):
    return HttpResponse("It's the main page")


def countries_by_medals(request, year, medal):
    year_filter = Statistics.objects.filter(games__year=year)

    if medal == "gold":
        result = year_filter.filter(medal__icontains='gold')
    elif medal == "silver":
        result = year_filter.filter(medal__icontains='silver')
    else:
        result = year_filter.filter(medal__icontains='bronze')

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
