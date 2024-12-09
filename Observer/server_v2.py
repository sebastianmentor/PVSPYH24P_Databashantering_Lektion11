import socket
import threading

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def join(self, client_socket):
        self.clients.append(client_socket)
        print(f"[{self.name}] Ny klient ansluten.")

    def leave(self, client_socket):
        self.clients.remove(client_socket)
        print(f"[{self.name}] Klient lämnade.")

    def broadcast(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    self.leave(client)

class ChatServer:
    def __init__(self, host="0.0.0.0", port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.rooms = {}  # Dict för att hantera olika rum

    def handle_client(self, client_socket):
        client_socket.send("Välkommen till servern! Ange ett chattrum att gå med i: ".encode())
        room_name = client_socket.recv(1024).decode().strip()

        if room_name not in self.rooms:
            self.rooms[room_name] = ChatRoom(room_name)

        room = self.rooms[room_name]
        room.join(client_socket)
        client_socket.send(f"Du har gått med i rummet: {room_name}\n".encode())

        while True:
            try:
                message = client_socket.recv(1024)
                if message:
                    full_message = f"[{room_name}] {message.decode()}".encode()
                    room.broadcast(full_message, client_socket)
            except:
                room.leave(client_socket)
                client_socket.close()
                break

    def start(self):
        print("Server startad...")
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Ny anslutning från: {address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    server = ChatServer()
    server.start()
