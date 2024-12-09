import socket
import threading

class ChatClient:
    def __init__(self, host="127.0.0.1", port=12345):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print(message)
            except:
                print("Anslutningen bröts.")
                self.client_socket.close()
                break

    def send_messages(self):
        while True:
            message = input("")
            self.client_socket.send(message.encode())

    def start(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Ansluten till servern på {self.host}:{self.port}")
        except:
            print("Kunde inte ansluta till servern.")
            return

        threading.Thread(target=self.receive_messages).start()
        self.send_messages()

if __name__ == "__main__":
    port = int(input("Ange port: "))
    client = ChatClient()
    client.start()
