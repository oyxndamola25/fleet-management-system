# consumer.py
import pika
import json

def callback(ch, method, properties, body):
    data = json.loads(body)
    print("Received:", data)
    # Save data to database (placeholder)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='vehicle_usage')

channel.basic_consume(queue='vehicle_usage', on_message_callback=callback, auto_ack=True)
print('Waiting for messages...')
channel.start_consuming()
