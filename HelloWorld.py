import time
import socket

hostname = socket.gethostname()

while True:
    print(f"[POD: {hostname}] Hello, World! I deployed this via ArgoCD!!")
    time.sleep(5)
