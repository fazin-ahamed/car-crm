import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
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
def test_architecture_diagram_accuracy(api_client):
    url = reverse('architecture-diagram')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'diagram' in response.data
    assert response.data['diagram'] is not None

@pytest.mark.django_db
def test_architecture_diagram_completeness(api_client):
    url = reverse('architecture-diagram')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'diagram' in response.data
    assert 'components' in response.data['diagram']
    assert 'relationships' in response.data['diagram']
    assert len(response.data['diagram']['components']) > 0
    assert len(response.data['diagram']['relationships']) > 0
