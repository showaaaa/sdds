# Generated by Django 4.1.5 on 2023-02-01 23:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ride', '0005_remove_ride_sharer_ride_sharer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='sharer',
            field=models.ManyToManyField(blank=True, related_name='share', to=settings.AUTH_USER_MODEL),
        ),
    ]
