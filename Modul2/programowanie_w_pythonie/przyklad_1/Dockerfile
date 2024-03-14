# Polecenie Docker FROM określa podstawowy obraz kontenera
# Nasz podstawowy obraz to Linux z preinstalowanym python-3.10
FROM python:3.10

# Ustawiamy zmienną środowiskową
ENV APP_HOME /app

# Ustawiamy katalog roboczy wewnątrz kontenera
WORKDIR $APP_HOME

# Kopiujemy inne pliki do katalogu roboczego kontenera
COPY . .

# Instalujemy zależności wewnątrz kontenera
RUN pip install -r requirements.txt

# Oznaczamy port, na którym aplikacja działa wewnątrz kontenera
EXPOSE 5000

# Uruchomiamy naszą aplikację wewnątrz kontenera
ENTRYPOINT ["python", "app.py"]