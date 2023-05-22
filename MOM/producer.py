import pika

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare a queue
queue_name = 'test_queue'
channel.queue_declare(queue=queue_name)

# Publish a message to the queue
message = 'Hello, World!'
channel.basic_publish(exchange='', routing_key=queue_name, body=message)

print("Sent message: {}".format(message))
connection.close()
