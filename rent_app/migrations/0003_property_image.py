# Generated by Django 5.0.1 on 2024-02-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0002_alter_property_price_alter_property_space'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(default='/media/defaults/default.png', upload_to='rent-images/%Y/%m/%d'),
        ),
    ]
