
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


class Guest(User):
    pass


class Hotel(models.Model):
    name = models.CharField(max_length=127)
    address = models.CharField(max_length=255)


class Room(models.Model):
    size = models.PositiveSmallIntegerField()
    floor = models.SmallIntegerField()
    label = models.CharField(max_length=63)
    status = models.CharField(max_length=1, choices=ROOM_STATUS)
    capacity = models.PositiveSmallIntegerField()

    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)


class Reservation(models.Model):
    begin = models.DateTimeField()
    end = models.DateTimeField()
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=RESERVATION_STATUS)
    receipt = models.FilePathField(path='/home/pluto/tmp/receipts', recursive=True, max_length=255)

    rooms = models.ManyToManyField(Room, related_name='reservations', related_query_name='reservations')
    guests = models.ManyToManyField(Guest, related_name='reservations', related_query_name='reservations')
