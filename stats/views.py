from django.db.models import Count, Q, Avg
from django.shortcuts import render

from stats.models import Statistics, Athlete


def index(request):
    return render(request, 'stats/index.html')


def q_athletes_by_age(request):
    return render(request, 'stats/q_athletes_by_age.html')


def q_athletes_by_medals(request):
    return render(request, 'stats/q_athletes_by_medals.html')


def q_athletes_by_weight(request):
    return render(request, 'stats/q_athletes_by_weight.html')


def q_countries_by_athletes_count(request):
    return render(request, 'stats/q_countries_by_athletes_count.html')


def q_countries_by_gold_medals(request):
    return render(request, 'stats/q_countries_by_gold_medals.html')


def q_countries_by_medals(request):
    return render(request, 'stats/q_countries_by_medals.html')


def q_mean_height(request):
    return render(request, 'stats/q_mean_height.html')


def q_sex_percentage(request):
    return render(request, 'stats/q_sex_percentage.html')


def q_sport_by_athlete_count(request):
    return render(request, 'stats/q_sport_by_athlete_count.html')


def add_data(request):
    return render(request, 'stats/add_data.html')


def add_player(request):
    return render(request, 'stats/add_player.html')


def add_olympiad(request):
    return render(request, 'stats/add_olympiad.html')


def add_athlete_result(request):
    return render(request, 'stats/add_athlete_result.html')


def delete_data(request):
    return render(request, 'stats/delete_data.html')


def countries_by_medals(request):
    year = request.GET.get("year")
    medal = request.GET.get("medal")
    if year:
        try:
            year = int(year)
        except:
            return render(request, 'stats/countries_by_medals.html')
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
        return render(request, 'stats/countries_by_medals.html')

    result = result.values('country_code__country_name') \
        .annotate(medals_count=Count('country_code')) \
        .order_by('-medals_count')

    if not result:
        return render(request, 'stats/countries_by_medals.html')

    context = {'res': result, 'color': medal, 'year': year}
    return render(request, 'stats/countries_by_medals.html', context)


def athletes_by_medals(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            return render(request, 'stats/athletes_by_medals.html')
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
        return render(request, 'stats/athletes_by_medals.html')

    context = {'res': result, 'year': year}
    return render(request, 'stats/athletes_by_medals.html', context)


def countries_by_athletes_count(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            return render(request, 'stats/countries_by_athletes_count.html')
        result = Statistics.objects.filter(games__year=year)
    else:
        result = Statistics.objects

    result = result.values('country_code__country_name') \
        .annotate(athlete_count=Count('player_id', distinct=True)) \
        .order_by('-athlete_count')

    if not result:
        return render(request, 'stats/countries_by_athletes_count.html')

    context = {'res': result, 'year': year}
    return render(request, 'stats/countries_by_athletes_count.html', context)


def sex_percentage(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            return render(request, 'stats/sex_percentage.html')
        res = Statistics.objects.filter(games__year=year)
    else:
        res = Statistics.objects

    female_count = res.filter(player_id__sex='F').values('player_id').distinct().count()
    male_count = res.filter(player_id__sex='M').values('player_id').distinct().count()

    if not female_count or not male_count:
        return render(request, 'stats/sex_percentage.html')

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
            return render(request, 'stats/sport_by_athlete_count.html')
        result = Statistics.objects.filter(games__year=year)
    else:
        result = Statistics.objects

    result = result.values('player_id__statistics__sport') \
        .annotate(athlete_count=Count('player_id', distinct=True)) \
        .order_by('-athlete_count')

    if not result:
        return render(request, 'stats/sport_by_athlete_count.html')

    context = {'res': result, 'year': year}
    return render(request, 'stats/sport_by_athlete_count.html', context)


def athletes_by_weight(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            return render(request, 'stats/athletes_by_weight.html')
        result = Statistics.objects.filter(games__year=year)
    else:
        result = Statistics.objects

    result = result.values('player_id__name', 'weight').order_by('-weight').distinct()

    if not result:
        return render(request, 'stats/athletes_by_weight.html')

    context = {'res': result, 'year': year}
    return render(request, 'stats/athletes_by_weight.html', context)


def athletes_by_age(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            return render(request, 'stats/athletes_by_age.html')
        result = Statistics.objects.filter(games__year=year)
    else:
        result = Statistics.objects

    result = result.exclude(age=-1).values('player_id__name', 'age').order_by('-age').distinct()

    if not result:
        return render(request, 'stats/athletes_by_age.html')

    context = {'res': result, 'year': year}
    return render(request, 'stats/athletes_by_age.html', context)


def countries_by_gold_medals(request):
    country_code = request.GET.get("country_code")
    if country_code:
        result = Statistics.objects.filter(country_code__country_code__icontains=country_code) \
            .filter(medal__icontains='gold') \
            .values('games_id').annotate(medal_count=Count('games_id')) \
            .order_by('-medal_count')
    else:
        result = None

    if not result:
        return render(request, 'stats/countries_by_gold_medals.html')

    context = {'res': result, 'country': country_code}
    return render(request, 'stats/countries_by_gold_medals.html', context)


def mean_height(request):
    year = request.GET.get("year")
    if year:
        try:
            year = int(year)
        except:
            return render(request, 'stats/mean_height.html')
        result = Athlete.objects.filter(statistics__games__year=year)
    else:
        result = Athlete.objects

    f = result.filter(sex__exact='F').exclude(height=-1)\
        .aggregate(Avg('height'))
    m = result.filter(sex__exact='M').exclude(height=-1)\
        .aggregate(Avg('height'))

    f['height__avg'] = round(f['height__avg'], 3)
    m['height__avg'] = round(m['height__avg'], 3)

    if not f or not m:
        return render(request, 'stats/mean_height.html')

    context = {'female_mean': f, 'male_mean': m, 'year': year}
    return render(request, 'stats/mean_height.html', context)


def delete_statistics_by_id(request, statistics_id):
    try:
        record = Statistics.objects.get(pk=statistics_id)
        record.delete()
    except:
        context = {'res': "delete unsuccessful"}
        return render(request, 'stats/delete_statistics_by_id.html', context)

    context = {'res': "delete successful"}
    return render(request, 'stats/delete_statistics_by_id.html', context)

