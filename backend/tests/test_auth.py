import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

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
def test_user_registration(api_client):
    url = '/api/auth/register/'
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert 'token' in response.data

@pytest.mark.django_db
def test_user_login(api_client, create_user):
    user = create_user('testuser', 'testpassword')
    url = '/api/auth/login/'
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200
    assert 'token' in response.data

@pytest.mark.django_db
def test_token_generation(api_client, create_user):
    user = create_user('testuser', 'testpassword')
    refresh = RefreshToken.for_user(user)
    assert 'access' in str(refresh.access_token)
    assert 'refresh' in str(refresh)
