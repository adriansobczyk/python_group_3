import pika  # Importowanie biblioteki pika do komunikacji z RabbitMQ
from datetime import datetime  # Importowanie modułu datetime do obsługi znaczników czasu
import sys  # Importowanie modułu sys do systemowych parametrów i funkcji
import json  # Importowanie modułu json do obsługi danych w formacie JSON

# Definiowanie poświadczeń RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')

# Ustanawianie połączenia z serwerem RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()  # Tworzenie kanału do komunikacji

# Deklarowanie bezpośredniej wymiany o nazwie 'task_mock'
channel.exchange_declare(exchange='task_mock', exchange_type='direct')

# Deklarowanie trwałej kolejki o nazwie 'task_queue' dla zadań
channel.queue_declare(queue='task_queue', durable=True)

# Wiązanie kolejki 'task_queue' z wymianą 'task_mock'
channel.queue_bind(exchange='task_mock', queue='task_queue')

# Definiowanie funkcji głównej
def main():
    # Iterowanie 5 razy w celu symulacji wysłania 5 zadań
    for i in range(5):
        # Tworzenie słownika wiadomości z szczegółami zadania
        message = {
            "id": i + 1,  # Identyfikator zadania
            "payload": f"Zadanie #{i + 1}",  # Opis zadania
            "date": datetime.now().isoformat()  # Bieżący znacznik czasu
        }

        # Publikowanie wiadomości do wymiany 'task_mock' z kluczem routingu 'task_queue'
        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=json.dumps(message).encode(),  # Konwersja wiadomości do formatu JSON
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # Zapewnienie trwałości wiadomości
            ))
        # Wyświetlanie potwierdzenia wysłania wiadomości
        print(" [x] Sent %r" % message)
    
    # Zamykanie połączenia
    connection.close()

# Wywoływanie funkcji głównej, jeśli skrypt jest uruchamiany bezpośrednio
if __name__ == '__main__':
    main()
