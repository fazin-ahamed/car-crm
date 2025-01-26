import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from backend.models import Vehicle, Booking, Customer, VehicleType, User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpass')

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

@pytest.fixture
def booking(user, vehicle):
    return Booking.objects.create(
        vehicle=vehicle,
        user=user,
        start_date='2023-01-01T10:00:00Z',
        end_date='2023-01-02T10:00:00Z',
        status='Pending'
    )

@pytest.fixture
def customer():
    return Customer.objects.create(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        phone='1234567890'
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

@pytest.mark.django_db
def test_create_booking(api_client, user, vehicle):
    url = reverse('booking-list')
    data = {
        'vehicle': vehicle.id,
        'user': user.id,
        'start_date': '2023-01-01T10:00:00Z',
        'end_date': '2023-01-02T10:00:00Z',
        'status': 'Pending'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Booking.objects.count() == 1
    assert Booking.objects.get().status == 'Pending'

@pytest.mark.django_db
def test_retrieve_booking(api_client, booking):
    url = reverse('booking-detail', args=[booking.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['status'] == booking.status

@pytest.mark.django_db
def test_update_booking(api_client, booking):
    url = reverse('booking-detail', args=[booking.id])
    data = {
        'vehicle': booking.vehicle.id,
        'user': booking.user.id,
        'start_date': '2023-01-01T10:00:00Z',
        'end_date': '2023-01-02T10:00:00Z',
        'status': 'Confirmed'
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    booking.refresh_from_db()
    assert booking.status == 'Confirmed'

@pytest.mark.django_db
def test_delete_booking(api_client, booking):
    url = reverse('booking-detail', args=[booking.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Booking.objects.count() == 0

@pytest.mark.django_db
def test_create_customer(api_client):
    url = reverse('customer-list')
    data = {
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane.smith@example.com',
        'phone': '0987654321'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Customer.objects.count() == 1
    assert Customer.objects.get().email == 'jane.smith@example.com'

@pytest.mark.django_db
def test_retrieve_customer(api_client, customer):
    url = reverse('customer-detail', args=[customer.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == customer.email

@pytest.mark.django_db
def test_update_customer(api_client, customer):
    url = reverse('customer-detail', args=[customer.id])
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone': '1234567890'
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    customer.refresh_from_db()
    assert customer.email == 'john.doe@example.com'

@pytest.mark.django_db
def test_delete_customer(api_client, customer):
    url = reverse('customer-detail', args=[customer.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Customer.objects.count() == 0
