# Generated by Django 5.0.6 on 2024-06-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_darktheme_delete_beats'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rank',
            field=models.CharField(default='basic', max_length=30),
        ),
    ]
