import pytest
import subprocess
import os

@pytest.mark.parametrize("script", [
    "build_script_1.sh",
    "build_script_2.sh",
    "build_script_3.sh"
])
def test_build_scripts(script):
    # Ensure the build script exists
    assert os.path.exists(script), f"Build script {script} does not exist."

    # Run the build script and capture the output
    result = subprocess.run(["/bin/bash", script], capture_output=True, text=True)

    # Check if the build script executed successfully
    assert result.returncode == 0, f"Build script {script} failed with return code {result.returncode}."

    # Check for specific output in the build script's output
    assert "Build completed successfully" in result.stdout, f"Build script {script} did not complete successfully. Output: {result.stdout}"
