from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import VehicleSerializer
from .models import Vehicle

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @action(detail=True, methods=['post'])
    def set_availability(self, request, pk=None):
        vehicle = self.get_object()
        availability = request.data.get('availability')
        if availability is not None:
            vehicle.availability = availability
            vehicle.save()
            return Response({'status': 'availability set'})
        else:
            return Response({'status': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
