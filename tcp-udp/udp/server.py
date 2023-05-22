import socket

class ChatServerUDP:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        print(f"Servidor de chat iniciado em {self.host}:{self.port}")

        self.receive_messages()

    def receive_messages(self):
        while True:
            message, client_address = self.server_socket.recvfrom(1024)
            print(f"Mensagem recebida de {client_address[0]}:{client_address[1]}: {message.decode('utf-8')}")
            
            if client_address not in self.clients:
                self.clients.append(client_address)

            self.broadcast(message, client_address)

    def broadcast(self, message, sender_address):
        for client_address in self.clients:
            if client_address != sender_address:
                self.server_socket.sendto(message, client_address)

if __name__ == "__main__":
    host = "localhost"
    port = 5001
    server = ChatServerUDP(host, port)
    server.start()
