import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def _create_user(username, password):
        user = User.objects.create_user(username=username, password=password)
        return user
    return _create_user

@pytest.mark.django_db
def test_data_encryption(api_client, create_user):
    user = create_user('testuser', 'testpassword')
    url = reverse('user-detail', args=[user.id])
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    assert 'password' not in response.data

@pytest.mark.django_db
def test_input_validation(api_client):
    url = reverse('user-list')
    data = {
        'username': 'testuser',
        'password': 'short'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'password' in response.data

@pytest.mark.django_db
def test_xss_protection(api_client, create_user):
    user = create_user('testuser', 'testpassword')
    url = reverse('user-detail', args=[user.id])
    api_client.force_authenticate(user=user)
    data = {
        'username': 'testuser',
        'first_name': '<script>alert("XSS")</script>'
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == 400
    assert 'first_name' in response.data
    assert 'XSS' not in response.data['first_name']
