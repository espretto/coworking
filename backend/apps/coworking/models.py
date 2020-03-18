
from django.db import models
from django.contrib.auth.models import User


class Client(User):
    """A fellow coworker

    Every coworker is a django user, but not every django user is a coworker.

    Attributes:
        id (int): id
        username (str): username
        first_name (str): first name
        last_name (str): last name
        date_joined (str): date coworker joined
        reservations (List[Reservation]): list of desk reservations
    """
    pass


class Workspace(models.Model):
    """Workspaces regroup offices under one roof

    Attributes:
        id (int): id
        name (str): name
        address (str): address
        latitude (decimal): geographic location (latitude)
        longitude (decimal): geographic location (longitude)
        offices (List[Office]): offices within this workspace
    """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=14, decimal_places=6)
    longitude = models.DecimalField(max_digits=15, decimal_places=6)


class Office(models.Model):
    """Offices have a limited number of desks for coworkers to reserve

    Attributes:
        id (int): id
        label (str): name/label
        size (int): number of square meters
        capacity (int): total number of desks
        workspace (Workspace): workspace of this office
        reservations (List[Reservation]): list of desk reservations
    """
    label = models.CharField(max_length=50)
    size = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    workspace = models.ForeignKey(Workspace, related_name='offices', on_delete=models.PROTECT)


class Reservation(models.Model):
    """Reservations are billable records of clients renting desks of an office

    Attributes:
        id (int): id
        begin (date): start date and time
        end (date): end date and time
        office (Office): the office of the coworker's desk
        client (Client): the coworker
    """
    begin = models.DateTimeField()
    end = models.DateTimeField()
    office = models.ForeignKey(Office, related_name='reservations', on_delete=models.PROTECT)
    client = models.ForeignKey(Client, related_name='reservations', on_delete=models.PROTECT)
