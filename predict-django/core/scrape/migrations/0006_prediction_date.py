# Generated by Django 4.0.6 on 2022-07-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0005_prediction'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='date',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]