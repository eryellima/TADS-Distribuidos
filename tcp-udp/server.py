import socket
import threading

class ChatServer:
    def __init__(self, host, tcp_port, udp_port):
        self.host = host
        self.tcp_port = tcp_port
        self.udp_port = udp_port
        self.tcp_server_socket = None
        self.udp_server_socket = None
        self.tcp_clients = []
        self.udp_clients = []

    def start(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.bind((self.host, self.tcp_port))
        self.tcp_server_socket.listen(5)
        print(f"Servidor de chat TCP iniciado em {self.host}:{self.tcp_port}")

        self.udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_server_socket.bind((self.host, self.udp_port))
        print(f"Servidor de chat UDP iniciado em {self.host}:{self.udp_port}")

        tcp_thread = threading.Thread(target=self.tcp_connections)
        udp_thread = threading.Thread(target=self.udp_connections)

        tcp_thread.start()
        udp_thread.start()

    def tcp_connections(self):
        while True:
            client_socket, client_address = self.tcp_server_socket.accept()
            print(f"Nova conexão TCP de {client_address[0]}:{client_address[1]}")
            client_thread = threading.Thread(target=self.handle_client_tcp, args=(client_socket,))
            client_thread.start()

    def handle_client_tcp(self, client_socket):
        self.tcp_clients.append(client_socket)
        while True:
            try:
                message = client_socket.recv(1024).decode("utf-8")
                if message:
                    print(f"Mensagem TCP recebida: {message}")
                    self.broadcast_tcp(message, client_socket)
                else:
                    self.remove_tcp_client(client_socket)
                    break
            except:
                self.remove_tcp_client(client_socket)
                break

    def broadcast_tcp(self, message, sender_socket):
        for client_socket in self.tcp_clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode("utf-8"))
                except:
                    self.remove_tcp_client(client_socket)

    def remove_tcp_client(self, client_socket):
        if client_socket in self.tcp_clients:
            self.tcp_clients.remove(client_socket)
        client_socket.close()

    def udp_connections(self):
        while True:
            message, client_address = self.udp_server_socket.recvfrom(1024)
            print(f"Mensagem UDP recebida de {client_address[0]}:{client_address[1]}: {message.decode('utf-8')}")

            if client_address not in self.udp_clients:
                self.udp_clients.append(client_address)

            self.broadcast_udp(message, client_address)

    def broadcast_udp(self, message, sender_address):
        for client_address in self.udp_clients:
            if client_address != sender_address:
                self.udp_server_socket.sendto(message, client_address)

if __name__ == "__main__":
    host = "localhost"
    tcp_port = 5000
    udp_port = 5001
    server = ChatServer(host, tcp_port, udp_port)
    server.start()
