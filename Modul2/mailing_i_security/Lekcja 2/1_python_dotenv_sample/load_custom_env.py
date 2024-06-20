from dotenv import load_dotenv
from pathlib import Path
import os


'''
Załadowanie zmiennych z pliku .env-dev z folderu sample_folder
'''

# Określenie ścieżki do pliku .env
BASE_DIR = Path(__file__).resolve().parent
dotenv_path = os.path.join(BASE_DIR, 'sample_folder/.env-dev')
load_dotenv(dotenv_path)

# Teraz możesz używać zmiennych środowiskowych w swoim kodzie
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
debug = os.getenv('DEBUG')

print(f"Database URL: {database_url}")
print(f"Secret Key: {secret_key}")
print(f"Debug Mode: {debug}")
