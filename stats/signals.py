from django.core.exceptions import BadRequest
from django.db.models import signals
from django.dispatch import receiver
from stats.models import Athlete, OlympiadInfo


@receiver(signals.pre_save, sender=Athlete)
def validate_data(sender, instance: Athlete, *args, **kwargs):
    if instance.height > 220 or instance.height < 120:
        raise BadRequest("Invalid height: must be in range [120, 220].")


@receiver(signals.pre_save, sender=OlympiadInfo)
def validate_data(sender, instance: OlympiadInfo, *args, **kwargs):
    if instance.year > 2022 or instance.year < 1896:
        raise BadRequest("Invalid year: must be in range [1896, 2022]")
