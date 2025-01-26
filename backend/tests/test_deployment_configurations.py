import pytest
import os

@pytest.mark.parametrize("config_file", [
    "docker-compose.yml",
    "nginx.conf",
    "uwsgi.ini"
])
def test_deployment_configurations(config_file):
    # Ensure the deployment configuration file exists
    assert os.path.exists(config_file), f"Deployment configuration file {config_file} does not exist."

    # Check for specific content in the deployment configuration file
    with open(config_file, 'r') as file:
        content = file.read()
        assert "version" in content or "server" in content or "[uwsgi]" in content, f"Deployment configuration file {config_file} does not contain expected content."
