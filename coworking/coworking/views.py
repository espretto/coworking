
from rest_framework import viewsets

from .models import Client, Workspace, Office, Reservation
from .serializers import ClientSerializer, WorkspaceSerializer, OfficeSerializer, ReservationSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows guests to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows guests to be viewed or edited.
    """
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows guests to be viewed or edited.
    """
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows guests to be viewed or edited.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer