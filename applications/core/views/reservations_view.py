from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.core.serializers.reservations_serializers import ReservationReadSerializer


class ReservationsView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReservationReadSerializer
    queryset = serializer_class.Meta.model.objects.all()

    @action(detail=False, methods=['get'])
    def get_reservations_with_previous(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

        # try:
        #     serialized_customer = self.service.activate_customer(pk)
        # except Http404 as ex:
        #     return Response(data=ex.args, status=status.HTTP_404_NOT_FOUND)
        # except (FireblocksApiException, ConnectionError) as ex:
        #     return Response(data=ex.args, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # else:
        #     return Response(data=serialized_customer, status=status.HTTP_200_OK)
