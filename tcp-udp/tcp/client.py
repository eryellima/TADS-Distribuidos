import socket
import threading

"""
    o cliente se conecta ao servidor especificado pelo endereço host e porta. apois isso com uso das thread separa para receber as mensagens e exibir elas na tela.
"""

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def start(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        while True:
            message = input()
            self.send_message(message)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                print(f"Mensagem recebida: {message}")
            except:
                print("Erro ao receber mensagem.")
                break

    def send_message(self, message):
        try:
            self.client_socket.send(message.encode("utf-8"))
        except:
            print("Erro ao enviar mensagem.")

if __name__ == "__main__":
    host = "localhost"
    port = 5000
    client = ChatClient(host, port)
    client.start()
