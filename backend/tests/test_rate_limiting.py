import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.core.cache import cache

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture(autouse=True)
def clear_cache():
    cache.clear()

@pytest.mark.django_db
def test_rate_limiting(api_client):
    url = reverse('vehicle-list')
    data = {
        'type': 'Sedan',
        'registration_number': 'XYZ789',
        'status': 'Available',
        'availability': True
    }

    # Make 5 requests within the rate limit
    for _ in range(5):
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    # Make 6th request which should be rate limited
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS
