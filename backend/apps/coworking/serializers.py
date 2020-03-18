
from rest_framework import serializers

from .models import Client, Workspace, Office, Reservation


class ClientSerializer(serializers.ModelSerializer):
    """Client model serializer for json rendering"""
    reservations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'date_joined', 'reservations']


class WorkspaceSerializer(serializers.ModelSerializer):
    """Workspace model serializer for json rendering"""
    offices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'address', 'latitude', 'longitude', 'offices']


class OfficeSerializer(serializers.ModelSerializer):
    """Office model serializer for json rendering"""
    reservations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Office
        fields = ['id', 'label', 'size', 'capacity', 'workspace', 'reservations']


class ReservationSerializer(serializers.ModelSerializer):
    """Reservation model serializer for json rendering"""
    client = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    office = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Reservation
        fields = ['begin', 'end', 'office', 'client']
