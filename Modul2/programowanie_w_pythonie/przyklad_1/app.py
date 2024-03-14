from flask import Flask

'''
Docker Desktop:
https://www.docker.com/products/docker-desktop/

Komendy:
docker info - aktualne informacje o dockerze, używany aby sprawdzić czy docker działa
docker run -it hello-world - uruchomienie kontenera z obrazem hello-world
docker run -d mongo - uruchomienie kontenera z obrazem mongo w tle
docker ps - lista uruchomionych kontenerów
docker ps -a - lista wszystkich kontenerów
docker exec -it <4_cyfry_sha> bin/sh - wejście do kontenera
docker stop <4_cyfry_sha> - zatrzymanie kontenera
docker start <4_cyfry_sha> - uruchomienie kontenera
docker rm <4_cyfry_sha> - usunięcie kontenera
docker run -p 27017:27017 -d mongo - uruchomienie kontenera z obrazem mongo i przekierowaniem portów
docker run -p 27017:27017 -v e/dbstorage:/data/db -d mongo - uruchomienie kontenera z obrazem mongo, przekierowaniem portów i utworzeniem woluminu
docker images - lista obrazów
docker build . -t flask_app - budowanie obrazu z pliku Dockerfile
docker run -itd -p 3000:5000 flask_app - uruchomienie kontenera z obrazem flask_app i przekierowaniem portów
'''

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    # app.run()
    app.run(debug=False, host='0.0.0.0')