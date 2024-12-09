import socket
import threading

# Anslut till servern
def start_client(port:int=None):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"  # Ersätt med serverns IP om det behövs
    port = port or 12345

    try:
        client_socket.connect((host, port))
        print(f"Ansluten till servern på {host}:{port}")
    except:
        print("Kunde inte ansluta till servern.")
        return

    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(message)
            except:
                print("Anslutningen till servern bröts.")
                client_socket.close()
                break

    def send_messages():
        while True:
            message = input("")
            client_socket.send(message.encode())

    threading.Thread(target=receive_messages).start()
    send_messages()


if __name__ == "__main__":
    port = int(input("Ange port att allokera: "))
    start_client()
