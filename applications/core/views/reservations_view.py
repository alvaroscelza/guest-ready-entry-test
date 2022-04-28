from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from applications.core.serializers.reservations_serializers import ReservationSerializer


class ReservationsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationSerializer
    queryset = serializer_class.Meta.model.objects.all()
