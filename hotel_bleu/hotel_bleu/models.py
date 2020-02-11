from django.db import models
from django.contrib.auth.models import User

ROOM_STATUS = (
  ('R', 'Ready'),
  ('D', 'Dirty'),
  ('C', 'Cleanup'),
  )

RESERVATION_STATUS = (
  ('N', 'New'),
  ('C', 'Confirmed'),
  ('A', 'Arrived'),
  ('C', 'CheckedOut'),
  )


class Hotel(models.Model):
    address = models.CharField(max_length=200)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField()
    etage = models.SmallIntegerField()
    label = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=ROOM_STATUS)
    capacity = models.PositiveSmallIntegerField()


class Reservation(models.Model):
    begin = models.DateTimeField()
    end = models.DateTimeField()
    paid = models.BooleanField(default=False)
    room = models.ForeignKey(Room, related_name='reservations', related_query_name='reservation', on_delete=models.PROTECT)
    status = models.CharField(max_length=1, choices=RESERVATION_STATUS)
    receipt = models.FilePathField(path='/home/pluto/tmp', recursive=True, max_length=250)


class Guest(User):
    models.ManyToManyField(Reservation, related_name='guests', related_query_name='guest')
    pass
