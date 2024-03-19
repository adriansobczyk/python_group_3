import os
import shutil
import sys
import concurrent.futures
import threading


# Słownik z rozszerzeniami plików i ich kategoriami
extensions_mapping = {
    'obrazy': ['JPEG', 'PNG', 'JPG', 'SVG'],
    'pliki wideo': ['AVI', 'MP4', 'MOV', 'MKV'],
    'dokumenty': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'CSV'],
    'muzyka': ['MP3', 'OGG', 'WAV', 'AMR'],
    'archiwa': ['ZIP', 'GZ', 'TAR']
}

# Lista z nieznanymi rozszerzeniami (zmienna współdzielona dla wątków)
unknown_extensions = []

# Funkcja do sortowania plików w folderze według rozszerzeń
def sort_files(folder):
    # Inicjalizacja słownika kategorii
    categories = {category: [] for category in extensions_mapping.keys()}
    
    # Iteracja przez pliki w folderze
    for root, dirs, files in os.walk(folder):
        for file in files:
            extension = os.path.splitext(file)[1].strip('.').upper()
            found_category = False
            
            # Sprawdzenie kategorii dla rozszerzenia
            for category, extensions in extensions_mapping.items():
                if extension in extensions:
                    categories[category].append(file)
                    found_category = True
                    break
            
            # Jeśli rozszerzenie nieznane, dodaj je do listy nieznanych rozszerzeń
            if not found_category:
                unknown_extensions.append(extension)
    
    # Sortowanie plików w kategoriach
    for category, files in categories.items():
        category_folder = os.path.join(folder, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        for file in files:
            source_file = os.path.join(folder, file)
            destination_file = os.path.join(category_folder, file)
            shutil.move(source_file, destination_file)
    
    return categories

# Funkcja przetwarzająca folder rekurencyjnie
def process_folder(folder):
    thread_id = threading.get_ident()
    print(f"Wątek {thread_id}: Przetwarzanie folderu {folder}")
    categories = sort_files(folder)
    print(f"Wątek {thread_id}: Zakończono przetwarzanie folderu {folder}")
    print("Kategorie plików:")
    for category, files in categories.items():
        print(f"{category}: {len(files)} plików")
    print("\nZnane rozszerzenia:")
    for ext in set(unknown_extensions):
        print(ext)
    print("\nNieznane rozszerzenia:")
    for ext in set(unknown_extensions):
        print(ext)

# concurrent.futures
# def main():
#     # Sprawdzenie poprawności liczby argumentów
#     if len(sys.argv) != 2:
#         print("Użycie: python sort.py <ścieżka_do_folderu>")
#         sys.exit(1)

#     # Pobranie ścieżki folderu z argumentu
#     folder_path = sys.argv[1]

#     # Sprawdzenie istnienia podanej ścieżki
#     if not os.path.exists(folder_path):
#         print("Podana ścieżka nie istnieje.")
#         sys.exit(1)

#     # Utworzenie puli wątków
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Uruchomienie przetwarzania folderu w osobnym wątku
#         future = executor.submit(process_folder, folder_path)
#         try:
#             # Pobranie wyniku lub obsłużenie wyjątku
#             result = future.result()
#         except Exception as e:
#             print(f"Błąd podczas przetwarzania folderu: {e}")

# threading
def main():
    # Sprawdzenie poprawności liczby argumentów
    if len(sys.argv) != 2:
        print("Użycie: python sort.py <ścieżka_do_folderu>")
        sys.exit(1)

    # Pobranie ścieżki folderu z argumentu
    folder_path = sys.argv[1]

    # Sprawdzenie istnienia podanej ścieżki
    if not os.path.exists(folder_path):
        print("Podana ścieżka nie istnieje.")
        sys.exit(1)

    # Utworzenie wątku przetwarzającego folder
    process_thread = threading.Thread(target=process_folder, args=(folder_path,))
    process_thread.start()
    process_thread.join()

if __name__ == "__main__":
    main()
