from dotenv import load_dotenv
import os


'''
Podstawowe użycie biblioteki python-dotenv
'''

# Załadowanie zmiennych z pliku .env
load_dotenv()

# Teraz możesz używać zmiennych środowiskowych w swoim kodzie
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
debug = os.getenv('DEBUG')

print(f"Database URL: {database_url}")
print(f"Secret Key: {secret_key}")
print(f"Debug Mode: {debug}")
