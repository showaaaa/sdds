from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

TYPE_CHOICES = (
    ("SUV", "SUV"),
    ("COMPACT", "COMPACT"),
    ("F1", "F1"),
    ("--", "--"),
)
# Create your models here.
class Ride(models.Model):
    rideOwner          = models.ForeignKey(User, related_name='rideOwner', on_delete=models.CASCADE)
    driver             = models.ForeignKey(User, related_name='driver', on_delete=models.CASCADE, null=True, blank=True)
    sharer             = models.ManyToManyField(get_user_model(), related_name='share', blank=True)
    
    destAddr           = models.CharField(max_length=50)
    date               = models.DateTimeField(help_text='Format: 2023-01-01 12:00')
    #time               = models.TimeField(auto_now=False)
    vehicleType        = models.CharField(max_length=20, choices=TYPE_CHOICES, default='--')
    numPeople          = models.IntegerField(default=1)
    shared             = models.BooleanField(default=False)
    specRequest        = models.CharField(max_length=200, blank=True)

    class STATUS(models.IntegerChoices):
        opened    = 1
        confirmed = 2
        completed = 3 
    status             = models.IntegerField(default=1, choices=STATUS.choices)

    def __str__(self):
        return self.destAddr

    def get_absolute_url(self):
        return reverse('ride-detail', kwargs={'pk': self.pk})
