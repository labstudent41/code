import socket
import ssl

server_port = 8000
server_ip = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

ssl_client_socket = context.wrap_socket(sock, server_hostname=server_ip)

try:
    ssl_client_socket.send(b"Hello from client.")
    response = ssl_client_socket.recv(1024)
    print("Recieved:", response.decode())
except ssl.SSLError as e:
    print("SSL Error:", e)
finally:
    ssl_client_socket.close()
