# Generated by Django 5.0.6 on 2024-06-23 15:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PayPalAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypal_email', models.CharField(max_length=255, unique=True)),
                ('paypal_password_hash', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.user')),
            ],
        ),
        migrations.CreateModel(
            name='CompteBancaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cb_name', models.CharField(max_length=255)),
                ('cb_number', models.CharField(max_length=50, unique=True)),
                ('cb_code', models.CharField(max_length=50)),
                ('cb_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.user')),
            ],
            options={
                'verbose_name': 'Compte Bancaire',
                'verbose_name_plural': 'Comptes Bancaires',
            },
        ),
    ]
