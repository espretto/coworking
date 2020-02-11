
from rest_framework import viewsets

from .models import Hotel, Room, Guest, Reservation
from .serializers import HotelSerializer, RoomSerializer, GuestSerializer, ReservationSerializer


class GuestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows guests to be viewed or edited.
    """
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class HotelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows guests to be viewed or edited.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows guests to be viewed or edited.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows guests to be viewed or edited.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer