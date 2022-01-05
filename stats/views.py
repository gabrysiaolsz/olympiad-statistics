from django.http import HttpResponse, Http404
from django.db.models import Count
from stats.models import Statistics


def index(request):
    return HttpResponse("It's the main page")


def countries_by_medals(request, year):
    result = Statistics.objects \
        .filter(games__year=year) \
        .filter(medal__icontains='gold') \
        .values('noc__region').annotate(medals_count=Count('noc'))\
        .order_by('-medals_count')

    if not result:
        raise Http404()
    return HttpResponse(result)
