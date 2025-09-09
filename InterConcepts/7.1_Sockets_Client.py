import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8000))
print("Connected on 127.0.0.1")
message = s.recv(64)
s.sendall(b"Hello from client!")
s.close()

print(f"Message Received from server: {message}")

# Note
#1. Socket Type
#2. TCP or UDP
#3. IP Address
#4. Address