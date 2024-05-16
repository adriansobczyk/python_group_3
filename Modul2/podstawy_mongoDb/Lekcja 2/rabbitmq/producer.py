import pika

def main():
    # Ustawienia poświadczeń dla połączenia RabbitMQ
    credentials = pika.PlainCredentials('guest', 'guest')
    # Tworzenie połączenia z serwerem RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    # Uzyskanie kanału komunikacyjnego
    channel = connection.channel()

    # Deklaracja kolejki o nazwie 'hello_world'
    channel.queue_declare(queue='hello_world')

    # Publikowanie wiadomości do kolejki 'hello_world'
    channel.basic_publish(exchange='', routing_key='hello_world', body='Hello world!'.encode())
    print(" [x] Sent 'Hello World!'")
    
    # Zamknięcie połączenia
    connection.close()

if __name__ == '__main__':
    main()
