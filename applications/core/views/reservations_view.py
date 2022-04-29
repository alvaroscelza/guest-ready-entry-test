from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.core.serializers.reservations_serializers import ReservationsWithPreviousSerializer


class ReservationsView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReservationsWithPreviousSerializer
    queryset = serializer_class.Meta.model.objects.all()

    @action(detail=False, methods=['get'])
    def get_reservations_with_previous(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
