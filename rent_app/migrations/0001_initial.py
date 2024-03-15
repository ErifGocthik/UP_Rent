# Generated by Django 5.0.1 on 2024-02-29 04:56

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
            name='Renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('logo', models.ImageField(upload_to='logos_of_Renters/%Y/%m/%d')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Директор')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(max_length=16, verbose_name='Цена')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('short_description', models.CharField(max_length=512, verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('phone_number', models.CharField(max_length=16, verbose_name='Телефон')),
                ('space', models.FloatField()),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_app.renter', verbose_name='Арендодатель')),
            ],
        ),
    ]
