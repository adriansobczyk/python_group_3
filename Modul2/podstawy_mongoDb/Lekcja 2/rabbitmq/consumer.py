import pika
import sys

def main():
    # Ustawienia poświadczeń dla połączenia RabbitMQ
    credentials = pika.PlainCredentials('guest', 'guest')
    # Tworzenie połączenia z serwerem RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    # Uzyskanie kanału komunikacyjnego
    channel = connection.channel()

    # Deklaracja kolejki o nazwie 'hello_world'
    channel.queue_declare(queue='hello_world')

    # Funkcja zwrotna (callback) do obsługi otrzymywania wiadomości
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # Rozpoczęcie konsumowania wiadomości z kolejki 'hello_world'
    channel.basic_consume(queue='hello_world', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    # Rozpoczęcie odbierania wiadomości
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
