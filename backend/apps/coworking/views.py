
from rest_framework import viewsets, generics, exceptions

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


class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        q = self.request.query_params
        week = q.get('week', None)
        office_id = q.get('office', None)
        client_id = q.get('client', None)
        workspace_id = q.get('workspace', None)

        lookup_params = dict()

        if week is not None:
            if not week.isdigit():
                raise exceptions.ValidationError("week has to be an integer")
            lookup_params['begin__week'] = int(week)
            # reservation end date forcibly is in same week

        if client_id:
            if not client_id.isdigit():
                raise exceptions.ValidationError("client id has to be an integer")
            lookup_params['client_id__exact'] = int(client_id)

        if office_id:
            if not office_id.isdigit():
                raise exceptions.ValidationError("office id has to be an integer")
            lookup_params['office_id__exact'] = int(office_id)

        if workspace_id:
            if not workspace_id.isdigit():
                raise exceptions.ValidationError("workspace id has to be an integer")
            lookup_params['office__workspace_id__exact'] = int(workspace_id)

        return Reservation.objects.filter(**lookup_params)
