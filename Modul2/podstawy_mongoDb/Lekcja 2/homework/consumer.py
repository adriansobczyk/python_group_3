import pika
import json
from mongoengine import connect
from models import Contact

# Połączenie z RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Deklaracja kolejki
channel.queue_declare(queue='contacts_queue')

# Połączenie z bazą danych MongoDB
connect('contacts_db')

# Funkcja symulująca wysyłanie wiadomości e-mail
def send_email(contact_id):
    # Funkcja stub - tutaj można dodać kod do wysyłania e-maili
    print(f"Sending email to contact with ID: {contact_id}")

# Funkcja callback wywoływana przy odbieraniu wiadomości z kolejki
def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']
    contact = Contact.objects.get(id=contact_id)
    send_email(contact_id)
    # Ustawienie pola logicznego na True po wysłaniu e-maila
    contact.email_sent = True
    contact.save()
    print(f" [x] Email sent to {contact.first_name} {contact.last_name}")

# Konsumowanie wiadomości z kolejki RabbitMQ
channel.basic_consume(queue='contacts_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
