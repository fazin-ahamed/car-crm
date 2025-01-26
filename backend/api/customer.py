from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerSerializer
from .models import Customer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
