import socket

def start_server(host='127.0.0.1', port=65432):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f'Server started, listening on {host}:{port}')
        s.listen()
        #Accept a connection
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                #Receive data from the client
                data = conn.recv(1024)
                if not data:
                    break
                #send data back as a response
                conn.sendall(data)

if __name__ == "__main__":
    start_server()