import pika


# Cria uma conex]ão bloqueante com o servidor
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Cria um canal na conexão
channel = connection.channel()

# Declara a fila de mensagens
channel.queue_declare(queue='fila')

# defeina a função que cserá chamada quando uma mensagem for recebida da fila
def callback(ch, method, properties, body):
    print("Mensagem recebida:", body.decode())


# Configura o consumidor para rebeber mensagem da fila, quando uma mensagem chega, a função 'callback' será chamada para processa-la e o parametro 'auto_ack=True' indica que as mensagens será automaticamente confirmada após ser consumidas
channel.basic_consume(queue='fila',
                      on_message_callback=callback, auto_ack=True)

# Printa mensagem enquanto agurda as mensagens
print("Aguardando mensagens...")

# Inicia  o consumo de mensagens. O consumidor fica em execu~çao indefinidamente até que seja interrompido manualmente. Quando uma mensagen chegar na fila, a função 'callback' será chamada.
channel.start_consuming()

# Fecha a conexão com o servidor
connection.close()
