# ------------------ INSTALACJA PAKIETÓW ------------------ #

# https://pypi.org/

# Jak zainstalować pip na Windows?
'''
    1. Czy pip jest zainstalowany?
        pip --version
    2. Jeśli nie, to użyj komendy:
        python -m ensurepip --default-pip
        Jeśli nie działa, to:
            python -m ensurepip --default-pip --user
        Jeśli nie działa, to:
            python -m ensurepip --default-pip --user --upgrade
    3. Sprawdź czy pip jest zainstalowany:
        pip --version
    4. Linki do informacji na temat instalacji pip:
        https://www.liquidweb.com/kb/install-pip-windows/
        https://www.liquidweb.com/kb/install-pip-osx/
        https://www.liquidweb.com/kb/install-pip-linux/
'''

# Jak zainstalować paczkę?
'''
    python --version
    pip --version
    pip install <nazwa_pakietu>
    pip install <nazwa_pakietu>==<wersja>
    pip install <nazwa_pakietu> --upgrade - dla aktualizacji pakietu
    pip install <nazwa_pakietu> --upgrade --force-reinstall - dla aktualizacji pakietu z wymuszeniem reinstalacji pakietu
    pip install <nazwa_pakietu> --upgrade --force-reinstall --no-cache-dir - dla aktualizacji pakietu z wymuszeniem reinstalacji pakietu i bez cache
    pip install <nazwa_pakietu> --upgrade --force-reinstall --no-cache-dir --no-deps - dla aktualizacji pakietu z wymuszeniem reinstalacji pakietu i bez cache i bez zależności
    pip install <nazwa_pakietu> --upgrade --force-reinstall --no-cache-dir --no-deps --user - dla aktualizacji pakietu z wymuszeniem reinstalacji pakietu i bez cache i bez zależności i instalacja tylko dla aktualnego użytkownika
'''

# Jak zainstalować paczkę na Linux?
'''
    sudo apt-get install python3-pip
    sudo apt-get install python3-<nazwa_pakietu>
'''

# Jak zainstalować paczkę na Mac?
'''
    brew install python3
    brew install python3-<nazwa_pakietu>
'''


# Jak zainstalować paczkę z pliku?
'''
    echo > requirements.txt - dla utworzenia pliku requirements.txt
    pip install -r requirements.txt - dla instalacji pakietu z pliku requirements.txt
    pip install -r requirements.txt --upgrade --force-reinstall - dla aktualizacji pakietu z wymuszeniem reinstalacji pakietu z pliku requirements.txt
'''
