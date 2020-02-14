
from django.db.models import *
from django.contrib.auth.models import User


class Client(User):
    pass


class Workspace(Model):
    name = CharField(max_length=100)
    address = CharField(max_length=250)
    latitude = DecimalField(max_digits=14, decimal_places=6)
    longitude = DecimalField(max_digits=15, decimal_places=6)


class Office(Model):
    label = CharField(max_length=50)
    size = PositiveSmallIntegerField()
    floor = SmallIntegerField()
    capacity = PositiveSmallIntegerField()
    workspace = ForeignKey(Workspace, related_name='offices', on_delete=PROTECT)


class Reservation(Model):
    begin = DateTimeField()
    end = DateTimeField()
    office = ForeignKey(Office, related_name='reservations', on_delete=PROTECT)
    client = ForeignKey(Client, related_name='reservations', on_delete=PROTECT)
