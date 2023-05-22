import socket
import threading

class ChatClientUDP:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def start(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.bind(("localhost", 0))  # Vincula o socket a um endereço local disponível

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        while True:
            message = input()
            self.send_message(message)

    def receive_messages(self):
        while True:
            try:
                message, server_address = self.client_socket.recvfrom(1024)
                print(f"Mensagem recebida: {message.decode('utf-8')}")
            except OSError:
                break

    def send_message(self, message):
        try:
            self.client_socket.sendto(message.encode("utf-8"), (self.host, self.port))
        except:
            print("Erro ao enviar mensagem.")
            
if __name__ == "__main__":
    host = "localhost"
    port = 5001
    client = ChatClientUDP(host, port)
    client.start()
