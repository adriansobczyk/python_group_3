import os
import subprocess


def get_current_directory():
    '''
    Pobieranie bieżącego katalogu za pomocą os.getcwd().
    '''
    current_directory = os.getcwd()
    return current_directory

def run_python_script_in_subdirectory():
    '''
    Uruchamianie pliku Python w podkatalogu za pomocą subprocess i os (Windows).
    '''
    current_directory = get_current_directory()
    print("Bieżący katalog:", current_directory)
    # Tworzenie ścieżki do pliku Python w podkatalogu
    print("Bieżący katalog:", current_directory)
    script_path = os.path.join(current_directory, "intro", "intro.py")
    if os.path.exists(script_path):
        # Uruchamianie pliku Python za pomocą subprocess
        subprocess.run(["python", script_path])
    else:
        print("Plik nie istnieje.")


def file_operations():
    # Pobieranie bieżącego katalogu
    current_directory = os.getcwd()
    print("Bieżący katalog:", current_directory)

    # Listowanie zawartości katalogu
    print("Zawartość katalogu:")
    for item in os.listdir(current_directory):
        item_path = os.path.join(current_directory, item)
        if os.path.isfile(item_path):
            print(f"Plik: {item}")
        elif os.path.isdir(item_path):
            print(f"Katalog: {item}")
