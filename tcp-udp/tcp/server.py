import socket
import threading

"""
    O servido aceita conexões de varios clientes. ele armazena as conexões em uma lista e utiliza threads para tratar cada cliente
"""

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Servidor de chat iniciado em {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Nova conexão de {client_address[0]}:{client_address[1]}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        self.clients.append(client_socket)
        while True:
            try:
                message = client_socket.recv(1024).decode("utf-8")
                if message:
                    print(f"Mensagem recebida: {message}")
                    self.broadcast(message, client_socket)
                else:
                    self.remove_client(client_socket)
                    break
            except:
                self.remove_client(client_socket)
                break

    def broadcast(self, message, sender_socket):
        for client_socket in self.clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode("utf-8"))
                except:
                    self.remove_client(client_socket)

    def remove_client(self, client_socket):
        if client_socket in self.clients:
            self.clients.remove(client_socket)
        client_socket.close()

if __name__ == "__main__":
    host = "localhost"
    port = 5000
    server = ChatServer(host, port)
    server.start()
