import subprocess
import time
import yaml

# Configuration
image_name = "img_ds_https_apache"
# new_tag = f"{base_image_name}:{int(time.time())}"   # unique tag using timestamp
container_name = "con_ds_https_apache"
dockerfile_path = "."  # Path to Dockerfile
compose_file = "docker-compose.yaml"
service_name = "apache"

# Generate timestamp tag (e.g. myapp:20251123_170712)
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


# Step 2: Update docker-compose.yml
with open(compose_file) as f:
    compose_data = yaml.safe_load(f)

compose_data["services"][service_name]["image"] = new_tag

with open(compose_file, "w") as f:
    yaml.dump(compose_data, f, default_flow_style=False)

print(f"Updated {compose_file} to use {new_tag}")


# Step 3: Stop and remove existing container
run_command(f"docker stop {container_name}")
run_command(f"docker rm {container_name}")

# Step 4: Redeploy with Docker Compose
run_command(f"docker compose up -d")




# Step 4: Run new container
#run_command(f"docker run -d --name {container_name} -p 443:443 {new_tag}")
