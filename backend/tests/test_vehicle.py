import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from backend.models import Vehicle, VehicleType

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def vehicle_type():
    return VehicleType.objects.create(name="Sedan", description="A small car")

@pytest.fixture
def vehicle(vehicle_type):
    return Vehicle.objects.create(
        type=vehicle_type,
        registration_number="ABC123",
        status="Available",
        availability=True
    )

@pytest.mark.django_db
def test_create_vehicle(api_client, vehicle_type):
    url = reverse('vehicle-list')
    data = {
        "type": vehicle_type.id,
        "registration_number": "XYZ789",
        "status": "Available",
        "availability": True
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Vehicle.objects.count() == 1
    assert Vehicle.objects.get().registration_number == "XYZ789"

@pytest.mark.django_db
def test_retrieve_vehicle(api_client, vehicle):
    url = reverse('vehicle-detail', args=[vehicle.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['registration_number'] == vehicle.registration_number

@pytest.mark.django_db
def test_update_vehicle(api_client, vehicle):
    url = reverse('vehicle-detail', args=[vehicle.id])
    data = {
        "type": vehicle.type.id,
        "registration_number": "UPDATED123",
        "status": "Unavailable",
        "availability": False
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    vehicle.refresh_from_db()
    assert vehicle.registration_number == "UPDATED123"
    assert vehicle.status == "Unavailable"
    assert vehicle.availability is False

@pytest.mark.django_db
def test_delete_vehicle(api_client, vehicle):
    url = reverse('vehicle-detail', args=[vehicle.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Vehicle.objects.count() == 0
