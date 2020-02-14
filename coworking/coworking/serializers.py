
from rest_framework import serializers

from .models import Client, Workspace, Office, Reservation

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client


class WorkspaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workspace


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
