from django.db import models
from django.urls import reverse

class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Maintenance'),
    ]

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=17, unique=True)
    license_plate = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    mileage = models.PositiveIntegerField()
    last_service_date = models.DateField()
    image = models.ImageField(upload_to='vehicle_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def get_absolute_url(self):
        return reverse('vehicle_detail', args=[str(self.id)])
