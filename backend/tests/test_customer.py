import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from backend.models.customer import Customer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def customer(user):
    return Customer.objects.create(user=user, phone='1234567890', address='123 Test St', city='Test City', state='Test State', country='Test Country', zip_code='12345')

def test_create_customer(api_client, user):
    data = {
        'user': user.id,
        'phone': '0987654321',
        'address': '456 Test Ave',
        'city': 'New City',
        'state': 'New State',
        'country': 'New Country',
        'zip_code': '67890'
    }
    response = api_client.post('/api/customers/', data)
    assert response.status_code == 201
    assert Customer.objects.count() == 2

def test_retrieve_customer(api_client, customer):
    response = api_client.get(f'/api/customers/{customer.id}/')
    assert response.status_code == 200
    assert response.data['phone'] == customer.phone

def test_update_customer(api_client, customer):
    data = {
        'phone': '1111111111',
        'address': '789 Test Blvd',
        'city': 'Updated City',
        'state': 'Updated State',
        'country': 'Updated Country',
        'zip_code': '54321'
    }
    response = api_client.put(f'/api/customers/{customer.id}/', data)
    assert response.status_code == 200
    customer.refresh_from_db()
    assert customer.phone == '1111111111'
    assert customer.address == '789 Test Blvd'

def test_delete_customer(api_client, customer):
    response = api_client.delete(f'/api/customers/{customer.id}/')
    assert response.status_code == 204
    assert Customer.objects.count() == 0
