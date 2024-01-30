# Magiczne Metody

## Lekcja 1

### 1. Wprowadzenie do "Magicznych" Metod

- Omówienie koncepcji "magicznych" metod w Pythonie.
- Wyjaśnienie roli "magicznych" metod w modyfikowaniu zachowania obiektów.

### 2. Metoda `__init__`

- Przedstawienie metody `__init__` i jej znaczenia w inicjalizacji obiektów.
- Omówienie przykładu z klasą `Human` demonstrującym użycie metody `__init__`.

### 3. Metody `__str__` i `__repr__`

- Wyjaśnienie roli metod `__str__` i `__repr__` w reprezentacji obiektów.
- Przedstawienie przykładów z klasami `Point` i `Human` ilustrujących użycie tych metod.

### 4. Metoda `__len__`

- Omówienie metody `__len__` i jej zastosowań w określaniu długości obiektów.
- Przedstawienie przykładu z klasą `MyList` prezentującym użycie metody `__len__`.

### 5. Metody `__getitem__` i `__setitem__`

- Wyjaśnienie roli metod `__getitem__` i `__setitem__` w dostępie i przypisywaniu wartości w obiektach.
- Przedstawienie przykładu z klasą `ListedValuesDict` demonstrującym zastosowanie tych metod.

### 6. Funktory i Metoda `__call__`

- Omówienie koncepcji funktorów i ich implementacji za pomocą metody `__call__`.
- Przedstawienie przykładu z klasą `Adder` ilustrującą wywoływanie obiektów jako funkcji.

### 7. Tworzenie niestandardowych Menedżerów Kontekstu

- Wyjaśnienie roli menedżerów kontekstu w zarządzaniu zasobami.
- Przedstawienie przykładu z klasą `Session` pokazującą tworzenie niestandardowych menedżerów kontekstu.

## Lekcja 2

### 8. **Tworzenie obiektu iteratora/generatora**

- Omówienie protokołu iteratora.
- Wyjaśnienie metod `__iter__()` i `__next__()`.

### **9. Tworzenie osobnego obiektu iteratora**

- Przykładowa implementacja klasy iteratora.
- Wykorzystanie dwóch klas: `Iterable` i `CustomIterator`.
- Praktyczne zastosowanie iteratora w pętli `for`.

### **10. Użycie generatorów**

- Omówienie generatorów jako efektywnego sposobu tworzenia iteratorów.
- Przykłady wykorzystania funkcji generującej z użyciem słowa kluczowego `yield`.

### **11. Enkapsulacja w Pythonie**

- Wyjaśnienie różnic między publicznymi, chronionymi i prywatnymi atrybutami/metodami.
- Przedstawienie konwencji nazewnictwa dla enkapsulacji.
- Praktyczne przykłady z wykorzystaniem klas i metod.

### **12. Getter/setter**

- Wyjaśnienie mechanizmu getterów i setterów.
- Przykłady użycia dekoratorów `@property`, `@<property_name>.setter`.

### **13. Zastępowanie operatorów matematycznych**

- Przegląd metod specjalnych do zastępowania operatorów matematycznych.
- Praktyczne przykłady definiowania własnych zachowań dla operatorów matematycznych.

### **14. Nadpisywanie operacji porównywania**

- Przedstawienie metod specjalnych związanych z operacjami porównywania.
- Przykłady implementacji metod porównujących dla własnych klas.
