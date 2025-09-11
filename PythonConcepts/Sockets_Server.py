import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen()
print("Started Listening on 127.0.0.1")

while True:
    client, address = s.accept()
    print("Client connected")
    client.send("Here is the response: data".encode())
    client.close()

# 

# Note
#1. Socket Type
#2. TCP or UDP
#3. IP Address
#4. Address