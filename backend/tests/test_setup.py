import pytest
from django.core.management import call_command
from django.conf import settings
import os

@pytest.mark.django_db
def test_setup_instructions():
    # Test if the setup instructions are correct and complete
    assert os.path.exists('docs/installation_and_configuration_guide.md')
    assert os.path.exists('docs/django-crm_user_guide.md')

    # Test if the setupdata command runs without errors
    call_command('setupdata')

    # Test if the initial data is loaded correctly
    from backend.models import VehicleType, Vehicle, Booking, Customer
    assert VehicleType.objects.exists()
    assert Vehicle.objects.exists()
    assert Booking.objects.exists()
    assert Customer.objects.exists()

    # Test if the superuser is created
    from django.contrib.auth.models import User
    assert User.objects.filter(is_superuser=True).exists()

    # Test if the development server runs without errors
    assert settings.DEBUG is True
    assert settings.ALLOWED_HOSTS == ['127.0.0.1']

    # Test if the admin site is accessible
    from django.urls import reverse
    from rest_framework.test import APIClient
    client = APIClient()
    url = reverse('admin:index')
    response = client.get(url)
    assert response.status_code == 200
