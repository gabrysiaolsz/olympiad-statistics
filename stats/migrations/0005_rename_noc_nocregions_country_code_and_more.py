# Generated by Django 4.0 on 2022-01-08 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_rename_noc_statistics_country_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nocregions',
            old_name='noc',
            new_name='country_code',
        ),
        migrations.RenameField(
            model_name='nocregions',
            old_name='region',
            new_name='country_name',
        ),
    ]
