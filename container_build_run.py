import subprocess
import time

# Configuration
image_name = "img_dumidu_apache"
# new_tag = f"{base_image_name}:{int(time.time())}"   # unique tag using timestamp
container_name = "con_dumidu_apache"
dockerfile_path = "."  # Path to Dockerfile

# Generate timestamp tag (e.g. myapp:20251123170712)
timestamp_tag = time.strftime("%Y%m%d_%H%M%S")
new_tag = f"{image_name}:{timestamp_tag}"


def run_command(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)
    return result

# Step 1: Build new image
run_command(f"docker build -t {new_tag} {dockerfile_path}")

# Step 2: Stop and remove existing container
run_command(f"docker stop {container_name}")
run_command(f"docker rm {container_name}")

# Step 3: Run new container
run_command(f"docker run -d --name {container_name} -p 8081:80 {new_tag}")
