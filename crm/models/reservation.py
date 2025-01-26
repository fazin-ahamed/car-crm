from django.db import models
from django.urls import reverse

class Reservation(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20)

    def __str__(self):
        return f'Reservation for {self.vehicle} by {self.customer}'

    def get_absolute_url(self):
        return reverse('reservation_detail', args=[str(self.id)])
