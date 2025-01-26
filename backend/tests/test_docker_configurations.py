import pytest
import os
import subprocess

@pytest.mark.parametrize("dockerfile", [
    "Dockerfile",
    "docker-compose.yml"
])
def test_docker_configurations(dockerfile):
    # Ensure the Docker configuration file exists
    assert os.path.exists(dockerfile), f"Docker configuration file {dockerfile} does not exist."

    # Check for specific content in the Docker configuration file
    with open(dockerfile, 'r') as file:
        content = file.read()
        assert "FROM" in content or "services:" in content, f"Docker configuration file {dockerfile} does not contain expected content."

    # Test Dockerfile by building the Docker image
    if dockerfile == "Dockerfile":
        result = subprocess.run(["docker", "build", "-f", dockerfile, "."], capture_output=True, text=True)
        assert result.returncode == 0, f"Dockerfile build failed with return code {result.returncode}. Output: {result.stdout} {result.stderr}"

    # Test docker-compose.yml by bringing up the services
    if dockerfile == "docker-compose.yml":
        result = subprocess.run(["docker-compose", "up", "-d"], capture_output=True, text=True)
        assert result.returncode == 0, f"docker-compose up failed with return code {result.returncode}. Output: {result.stdout} {result.stderr}"

        # Tear down the services after testing
        subprocess.run(["docker-compose", "down"], capture_output=True, text=True)
