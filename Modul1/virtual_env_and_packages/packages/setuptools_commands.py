'''
Przed instalacją upewnij się, że folder dist oraz math_operations.egg-info są usunięte.

Kroki do instalacji oraz stworzenia paczki:
1. python setup.py sdist (pamiętaj, że nazwa paczki musi być ta sama co nazwa folderu)
2. my_venv\Scripts\activate.bat (aktywacja wirtualnego środowiska na Windows) albo source my_venv/bin/activate (aktywacja wirtualnego środowiska na Linuxie)
3.  pip install -e . (w trybie developerskim/edytowalnym) albo pip install dist/math_operations-0.1.tar.gz.
4. pip list (sprawdź czy paczka się zainstalowała)
5. Przejdź do pliku my_pkg.py i uruchom go.
'''