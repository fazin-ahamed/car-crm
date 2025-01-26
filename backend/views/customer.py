from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CustomerSerializer
from .models import Customer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['post'])
    def set_status(self, request, pk=None):
        customer = self.get_object()
        status = request.data.get('status')
        if status is not None:
            customer.status = status
            customer.save()
            return Response({'status': 'status set'})
        else:
            return Response({'status': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
