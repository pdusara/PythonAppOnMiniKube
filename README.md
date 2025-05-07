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
