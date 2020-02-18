
from django.db import models
from django.contrib.auth.models import User


class Client(User):
    pass


class Workspace(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=14, decimal_places=6)
    longitude = models.DecimalField(max_digits=15, decimal_places=6)


class Office(models.Model):
    label = models.CharField(max_length=50)
    size = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    workspace = models.ForeignKey(Workspace, related_name='offices', on_delete=models.PROTECT)


class Reservation(models.Model):
    begin = models.DateTimeField()
    end = models.DateTimeField()
    office = models.ForeignKey(Office, related_name='reservations', on_delete=models.PROTECT)
    client = models.ForeignKey(Client, related_name='reservations', on_delete=models.PROTECT)
