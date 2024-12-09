import socket
import threading

# Starta server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "0.0.0.0"  # Lyssna på alla nätverksgränssnitt
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server startad på {host}:{port}")

    clients = []

    def broadcast(message, sender_socket):
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    clients.remove(client)

    def handle_client(client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                if message:
                    broadcast(message, client_socket)
            except:
                clients.remove(client_socket)
                client_socket.close()
                break

    while True:
        client_socket, address = server_socket.accept()
        print(f"Ny anslutning: {address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    start_server()
