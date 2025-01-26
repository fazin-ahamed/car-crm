import os
import pytest
from django.conf import settings

@pytest.mark.django_db
def test_environment_variables():
    # Test if environment variable templates exist
    assert os.path.exists('.env.example')
    assert os.path.exists('.env')

    # Test if environment variables are loaded correctly
    assert settings.SECRET_KEY is not None
    assert settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql'
    assert settings.DATABASES['default']['NAME'] == 'transport_rental_db'
    assert settings.DATABASES['default']['USER'] == 'transport_rental_user'
    assert settings.DATABASES['default']['PASSWORD'] == 'password'
    assert settings.DATABASES['default']['HOST'] == 'localhost'
    assert settings.DATABASES['default']['PORT'] == '5432'

    # Test if other environment variables are set correctly
    assert settings.DEBUG is False
    assert settings.ALLOWED_HOSTS == ['127.0.0.1', 'localhost']
    assert settings.EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend'
    assert settings.EMAIL_HOST == 'smtp.example.com'
    assert settings.EMAIL_PORT == 587
    assert settings.EMAIL_USE_TLS is True
    assert settings.EMAIL_HOST_USER == 'user@example.com'
    assert settings.EMAIL_HOST_PASSWORD == 'password'
