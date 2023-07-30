import pika



# Cria uma conexão bloqueante com o servidor RabbitMQ que está executando no localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Cria um canal na conexão
channel = connection.channel()

#Declara a fila chamada 'fila'
channel.queue_declare(queue='fila')

# Envia mensagens para a fila
def publicador():
    while True:
        mensagem = input("Digite uma mensagem ou 'sair' para encerrar o programa: ")

        if mensagem == "sair":
            break

        # publica a mensagem na fila declarada
        # O parâmetro 'exchange' é vazio, então a mensagem será enviada diretamente para a fila especificada em 'routing_key'
        channel.basic_publish(
            exchange='', routing_key='fila', body=mensagem)
        
    print("Publicador encerrado.")

# Verifica se o script está sendo executado diretamente e não sendo importado como um módulo
if __name__ == "__main__":
    publicador()

# Fecha a conexão com o servidor RabbitMQ    
connection.close()
