# Użyj obrazu Pythona w wersji 3.10
FROM python:3.10

# Definicja zmiennych środowiskowych i katalogu roboczego
ENV FLASK_APP=app.py
WORKDIR /app

# Kopiowanie plików aplikacji do kontenera
COPY . /app

# Instalacja zależności Pythona
RUN pip install -r requirements.txt

# Eksponowanie portu, na którym działa aplikacja Flask
EXPOSE 5000

# Dodanie woluminu do przechowywania pliku bazy danych SQLite
VOLUME /app/db

# Uruchamianie aplikacji Flask
CMD ["flask", "run", "--host=0.0.0.0"]