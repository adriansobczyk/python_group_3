 #-------------------- TWORZENIE ŚRODOWISKA WIRTUALNEGO --------------------#
'''
 Wirtualne środowisko jest to środowisko, które jest niezależne od innych
 środowisk i od systemu operacyjnego. Wirtualne środowisko pozwala na
 instalowanie pakietów i bibliotek, które są niezależne od innych
 środowisk i systemu operacyjnego. Wirtualne środowisko pozwala na
 instalowanie różnych wersji pakietów i bibliotek w różnych środowiskach.
'''

# Tworzenie środowiska wirtualnego na Windowsie:
'''
    1. Otwieramy konsolę systemową (cmd.exe)
    2. Wpisujemy komendę: py -m venv <nazwa_srodowiska>.
    3. Aby aktywować wpisujemy komendę: nazwa_środowiska\Scripts\activate.bat (np. venv\Scripts\activate.bat).
    4. Aby dezaktywować wpisujemy komendę: deactivate
'''

# Tworzenie środowiska wirtualnego na Linuxie:
'''
    1. Otwieramy terminal.
    2. Wpisujemy komendę: python3 -m venv <nazwa_srodowiska>.
    3. Aby aktywować wpisujemy komendę: source nazwa_środowiska/bin/activate (np. source venv/bin/activate).
    4. Aby dezaktywować wpisujemy komendę: deactivate
'''

# Jak sprawdzić ścieżkę do interpretera Pythona w środowisku wirtualnym?
'''
    1. Otwieramy konsolę systemową (cmd.exe).
    2. Aktywujemy środowisko wirtualne.
    3. Wpisujemy komendę: where python
'''

