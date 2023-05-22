import pika

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare a queue
queue_name = 'test_queue'
channel.queue_declare(queue=queue_name)

# Define a callback function for handling messages
def callback(ch, method, properties, body):
    print("Received message: {}".format(body.decode()))

# Consume messages from the queue
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()
