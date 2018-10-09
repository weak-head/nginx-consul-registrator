# nginx-consul-registrator

# Overview

TBD

# Build and Deploy

```bash
# Set hostname IP to the HOST_NAME variable:
export HOST_NAME=$(hostname -I | cut -d ' ' -f1)

# Pull the pre-requisite images:
docker-compose pull consul registrator

# Build the dependent images:
docker-compose build

# Start the containers in the detached mode:
docker-compose up -d

# Verify the running web-ui instances:
curl http://${HOST_NAME}:8500/v1/catalog/service/web-ui

# Check the consul ui via browser:
xdg-open http://${HOST_NAME}:8500

# Check the main ui via browser:
xdg-open http://${HOST_NAME}

# Check the logs of nginx gateway, consul and registrator:
docker logs nginx
docker logs consul
docker logs registrator

# Scale up the web-ui and system service:
docker-compose up -d --scale web-up=3 --scale system=3

# check the system service status
curl http://${HOST_NAME}/system/status

# Stop recovery service and verify the behavior.
# (run `docker ps` to get the exact name)
docker stop nginx-consul-registrator_recovery_1

# check the system service status
curl http://${HOST_NAME}/system/status
```