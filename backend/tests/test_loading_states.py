import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from backend.models import Vehicle, Booking, Customer, User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def vehicle():
    return Vehicle.objects.create(
        type='Sedan',
        registration_number='ABC123',
        status='Available',
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
def test_loading_state_vehicle_list(api_client):
    url = reverse('vehicle-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'loading' in response.data

@pytest.mark.django_db
def test_loading_state_vehicle_detail(api_client, vehicle):
    url = reverse('vehicle-detail', args=[vehicle.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'loading' in response.data

@pytest.mark.django_db
def test_loading_state_booking_list(api_client):
    url = reverse('booking-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'loading' in response.data

@pytest.mark.django_db
def test_loading_state_booking_detail(api_client, booking):
    url = reverse('booking-detail', args=[booking.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'loading' in response.data

@pytest.mark.django_db
def test_loading_state_customer_list(api_client):
    url = reverse('customer-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'loading' in response.data

@pytest.mark.django_db
def test_loading_state_customer_detail(api_client, customer):
    url = reverse('customer-detail', args=[customer.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'loading' in response.data
