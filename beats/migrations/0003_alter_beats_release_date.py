# Generated by Django 5.0.6 on 2024-06-21 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0002_alter_beats_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beats',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 16, 11, 26, 650008)),
        ),
    ]