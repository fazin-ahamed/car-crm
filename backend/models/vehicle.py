from django.db import models

class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Vehicle(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
