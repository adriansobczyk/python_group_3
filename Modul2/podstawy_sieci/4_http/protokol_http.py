'''
ETAPY ZAPYTANIA HTTP

    +---------------------+              +-----------------------+               +-------------------+
    |   Przeglądarka      |              |  Serwer DNS           |               |      Serwer       |
    +---------------------+              +-----------------------+               +-------------------+
                |                                    |                                    |
                | 1. Wysyła żądanie DNS              |                                    |
                |----------------------------------->|                                    |
                |                                    | 2. Zwraca adres IP                |
                |                                    |<-----------------------------------|
                |                                    |                                    |
                | 3. Nawiązuje połączenie            |                                    |
                |----------------------------------->|                                    |
                |                                    |                                    |
                | 4. Wysyła zapytanie HTTP           |                                    |
                |----------------------------------->|                                    |
                |                                    |                                    |
                |                                    | 5. Przetwarza zapytanie            |
                |                                    |                                    |
                |                                    | 6. Zwraca odpowiedź HTTP           |
                |                                    |<-----------------------------------|
                |                                    |                                    |
                |                                    |                                    |
                |                                    |                                    |
                | 7. Oczekuje na odpowiedź           |                                    |
                |<-----------------------------------|                                    |
                |                                    |                                    |
                | 8. Odbiera odpowiedź              |                                    |
                |<-----------------------------------|                                    |
                |                                    |                                    |
                | 9. Wyświetla zasoby               |                                    |
                |                                    |                                    |
                +---------------------+----------------------+---------------------+-------------------+
    
TYPY ZAPYTAŃ HTTP:

    GET - pobranie zasobu
    POST - wysłanie danych do serwera
    PUT - aktualizacja zasobu
    DELETE - usunięcie zasobu
    HEAD - pobranie nagłówka zasobu
    PATCH - aktualizacja części zasobu
    OPTIONS - informacje o metodach HTTP

NAGŁÓWEK ZAPYTANIA HTTP

    GET /other-19 HTTP/1.1 - metoda, ścieżka, wersja protokołu
    Host: www.example.com - nazwa hosta serwera docelowego
    User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729) - informacje o przeglądarce i systemie operacyjnym użytkownika
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 - typy MIME akceptowane przez przeglądarkę użytkownika
    Accept-Language: ru,en-us;q=0.7,en;q=0.3 - języki akceptowane przez przeglądarkę użytkownika
    Accept-Encoding: gzip,deflate - metody kompresji akceptowane przez przeglądarkę użytkownika
    Accept-Charset: windows-1251,utf-8;q=0.7,*;q=0.7 - zestaw znaków akceptowany przez przeglądarkę użytkownika
    Keep-Alive: 300 - czas, przez jaki połączenie ma być utrzymywane w stanie Keep-Alive (w sekundach)
    Connection: keep-alive - informacja o tym, czy połączenie ma być utrzymywane w stanie Keep-Alive (keep-alive) czy nie (close)

'''


from threading import Thread
from time import sleep
from http import client
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        pass

httpd = HTTPServer(('localhost', 8001), SimpleHTTPRequestHandler)
server = Thread(target=httpd.serve_forever)
server.start()
sleep(0.5)

h1 = client.HTTPConnection('localhost', 8001)
h1.request("GET", "/")

res = h1.getresponse()
print(res.status, res.reason)
data = res.read()
print(data)

httpd.shutdown()

'''
URL VS URI:

URI:
mailto:janek@example.com
ftp://ftp.example.com/docs/document.pdf
urn:isbn:0451450523

URL:
http://www.example.com/index.html
https://www.example.com/images/picture.jpg
ftp://ftp.example.com/docs/document.pdf
'''