# Generated by Django 4.1.5 on 2023-02-01 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destAddr', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('vehicleType', models.CharField(max_length=20)),
                ('numPeople', models.IntegerField(default=1, null=True)),
                ('isJoinable', models.BooleanField(default=False)),
                ('otherInfo', models.CharField(max_length=200, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Start'), (2, 'Confirmed'), (3, 'Completed')], default=1)),
                ('driverID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driverID', to=settings.AUTH_USER_MODEL)),
                ('rideOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rideOwner', to=settings.AUTH_USER_MODEL)),
                ('shareID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shareID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]