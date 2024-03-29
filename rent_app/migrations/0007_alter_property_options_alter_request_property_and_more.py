# Generated by Django 5.0.1 on 2024-02-29 09:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0006_alter_renter_options_request'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ('-id',), 'verbose_name': 'Недвижимость', 'verbose_name_plural': 'Недвижимость'},
        ),
        migrations.AlterField(
            model_name='request',
            name='property',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rent_app.property', verbose_name='Недвижимость'),
        ),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
