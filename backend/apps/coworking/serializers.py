
from rest_framework import serializers

from .models import Client, Workspace, Office, Reservation


class ClientSerializer(serializers.ModelSerializer):
    reservations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'date_joined', 'reservations']


class WorkspaceSerializer(serializers.ModelSerializer):
    offices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Workspace
        fields = ['name', 'address', 'latitude', 'longitude', 'offices']


class OfficeSerializer(serializers.ModelSerializer):
    reservations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Office
        fields = ['label', 'size', 'capacity', 'workspace', 'reservations']


class ReservationSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    office = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Reservation
        fields = ['begin', 'end', 'office', 'client']
