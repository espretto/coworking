
from rest_framework import serializers

from .models import Hotel, Room, Reservation, Guest


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'address', 'rooms']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['size', 'floor', 'label', 'status', 'capacity', 'hotel']


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'email', 'date_joined']


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ['begin', 'end', 'paid', 'status', 'rooms', 'guests']
