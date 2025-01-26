from django import forms
from crm.models.vehicle import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'vin', 'license_plate', 'status', 'mileage', 'last_service_date', 'image']
