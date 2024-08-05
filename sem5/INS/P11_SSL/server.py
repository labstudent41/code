import socket
import ssl

port = 4423
certfile = 'localhost.crt'
keyfile = 'localhost.key'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.listen(5)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile, keyfile)
print("Server Listening at port", port)

while True:
    client_socket, client_address = server_socket.accept()
    ssl_client_socket = context.wrap_socket(client_socket, server_side=True)

    try:
        data = ssl_client_socket.recv(1024)
        if data:
            print("Recieved:", data.decode())
            ssl_client_socket.send(b"Hello from server.")
    except ssl.SSLError as e:
        print("SSL Error:", e)
    finally:
        ssl_client_socket.close()
