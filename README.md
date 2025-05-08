# HelloWorld Python App on MiniKube

This project demonstrates a simple Python application that runs inside a Docker container and prints "Hello, World!" along with the hostname of the pod it is running on. It is designed to be deployed on a Kubernetes cluster using MiniKube with is load balanced.

## Features
- A Python script (`HelloWorld.py`) that continuously prints messages to the console.
- Dockerized application for easy deployment.
- Kubernetes deployment and service definitions for running the app in a cluster.
- CI/CD pipeline using GitHub Actions.

## Prerequisites
- [Docker](https://www.docker.com/) installed on your machine.
- [MiniKube](https://minikube.sigs.k8s.io/docs/) installed and configured.
- [kubectl](https://kubernetes.io/docs/tasks/tools/) CLI installed.

## How to Use

### 1. Build the Docker Image
Run the following command to build the Docker image:
```sh
docker build -t my-python-app:latest .

Here’s the updated README.md with the rest of the steps documented:

```markdown
# HelloWorld Python App on MiniKube

This project demonstrates a simple Python application that runs inside a Docker container and prints "Hello, World!" along with the hostname of the pod it is running on. It is designed to be deployed on a Kubernetes cluster using MiniKube with is load balanced.

## Features
- A Python script (`HelloWorld.py`) that continuously prints messages to the console.
- Dockerized application for easy deployment.
- Kubernetes deployment and service definitions for running the app in a cluster.

## Prerequisites
- [Docker](https://www.docker.com/) installed on your machine.
- [MiniKube](https://minikube.sigs.k8s.io/docs/) installed and configured.
- [kubectl](https://kubernetes.io/docs/tasks/tools/) CLI installed.

## CI/CD Pipeline
This project includes a CI/CD pipeline implemented using GitHub Actions. The pipeline automates the following steps:
1. **Build Stage**:
   - Builds a Docker image for the application.
   - Pushes the image to the GitHub Container Registry (`ghcr.io`).
2. **Deploy Stage**:
   - Starts MiniKube and sets the Kubernetes context.
   - Pulls the Docker image into MiniKube.
   - Deploys the application to the MiniKube cluster using Kubernetes manifests.
   - Verifies the deployment, service, and pod status.
   - Validates the application logs to ensure the expected output.

### Known Issue
An issue was encountered during the pipeline implementation: **MiniKube does not persist across stages in GitHub Actions**. This means that MiniKube's state is reset between the `build` and `deploy` stages. As a result:
- Post-deployment tests, such as verifying logs and pod status, had to be integrated into the `deploy` stage instead of being run as a separate `test` stage.

This limitation was addressed by combining deployment and testing into a single stage, ensuring the pipeline remains functional.


## How to Use

### 1. Build the Docker Image
Run the following command to build the Docker image:
```sh
docker build -t my-python-app:latest .
```

### 2. Start MiniKube
Ensure MiniKube is running:
```sh
minikube start
```

### 3. Load the Docker Image into MiniKube
Load the Docker image into MiniKube:
```sh
minikube image load my-python-app:latest
```

### 4. Deploy the Application
Apply the Kubernetes deployment and service definitions:
```sh
kubectl apply -f deployment-definition.yaml
kubectl apply -f service-definition.yaml
```

### 5. Access the Application Logs
To view the logs of the pod:
```sh
kubectl get pods -A
kubectl logs pod/<Pod-Name>
```
This will show the application logs.

### 6. Clean Up
To remove the application from the cluster, run:
```sh
kubectl delete -f deployment-definition.yaml
kubectl delete -f service-definition.yaml
```
