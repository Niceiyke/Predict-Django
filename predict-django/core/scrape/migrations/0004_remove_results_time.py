# Generated by Django 4.0.6 on 2022-07-23 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0003_alter_results_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='time',
        ),
    ]