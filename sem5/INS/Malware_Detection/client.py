import socket

server_port = 8888
server_ip = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))

sock.send(b"Ranjit coming")
response = sock.recv(1024)
print("Recieved:", response.decode())
