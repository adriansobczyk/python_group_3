from dotenv import load_dotenv
from pathlib import Path
import os

'''
Nadpisanie zmiennych środowiskowych z pliku .env-dev z folderu sample_folder
'''

load_dotenv(override=True)

database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
debug = os.getenv('DEBUG')

print(f"Database URL: {database_url}")
print(f"Secret Key: {secret_key}")
print(f"Debug Mode: {debug}")
