# producer.py

import pika
import json
from faker import Faker
from mongoengine import connect
from models import Contact

# Połączenie z RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Deklaracja kolejki
channel.queue_declare(queue='contacts_queue')

# Połączenie z bazą danych MongoDB
connect('contacts_db')

# Faker do generowania fałszywych danych
fake = Faker()

# Tworzenie fałszywych kontaktów i umieszczanie ich w kolejce RabbitMQ
def generate_contacts(num_contacts):
    for _ in range(num_contacts):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        contact = Contact(first_name=first_name, last_name=last_name, email=email)
        contact.save()
        message = {
            'contact_id': str(contact.id)
        }
        channel.basic_publish(exchange='', routing_key='contacts_queue', body=json.dumps(message))
        print(f" [x] Sent {message}")

generate_contacts(10)

connection.close()
