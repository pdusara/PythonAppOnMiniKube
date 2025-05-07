import time
import socket

hostname = socket.gethostname()

while True:
    print(f"[POD: {hostname}] Hello, World!")
    time.sleep(5)
