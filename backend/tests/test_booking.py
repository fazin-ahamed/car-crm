import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from backend.models import Booking, Vehicle, User

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
