from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import BookingSerializer
from .models import Booking

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=True, methods=['post'])
    def set_status(self, request, pk=None):
        booking = self.get_object()
        status = request.data.get('status')
        if status is not None:
            booking.status = status
            booking.save()
            return Response({'status': 'status set'})
        else:
            return Response({'status': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
