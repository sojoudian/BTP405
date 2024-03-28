import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))
        # Send a message
        s.sendall(b'Hello, server!')
        # Receive a response
        data = s.recv(1024)
        print(f'Received from server: {data.decode()}')

if __name__ == "__main__":
    start_client()
    