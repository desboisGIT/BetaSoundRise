# Generated by Django 5.0.6 on 2024-06-21 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beats',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 16, 2, 47, 256480)),
        ),
    ]