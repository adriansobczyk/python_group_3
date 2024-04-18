'''
Relacje w SQL:

1. Relacja jeden do jednego
+----------------+       +-------------------+
|     Osoba      |       |    DaneOsobowe    |
+----------------+       +-------------------+
| OsobaID (PK)   |       | DaneOsoboweID (PK)|
|                |       | OsobaID (FK)      |
|                |       | Adres             |
|                |       | Telefon           |
+----------------+       +-------------------+

2. Relacja jeden do wielu
+----------------+       +-------------------+
|     Klient     |       |     Zamówienia    |
+----------------+       +-------------------+
| KlientID (PK)  |       | ZamówienieID (PK)|
|                |       | KlientID (FK)    |
|                |       | Produkt           |
|                |       | Data              |
+----------------+       +-------------------+


3. Relacja wiele do wielu

+----------------+       +-------------------+       +------------------+
|     Klient     |       |    Produkty       |       |     Zamówienia    |
+----------------+       +-------------------+       +------------------+
| KlientID (PK)  |       | ProduktID (PK)   |       | ZamówienieID (PK)|
|                |       | Nazwa             |       |                  |
|                |       | Cena              |       |                  |
+----------------+       +-------------------+       +------------------+
                           | KlientID (FK)    |       | KlientID (FK)    |
                           | ProduktID (FK)   |       | ProduktID (FK)   |
                           +-------------------+       +------------------+

4. Relacja wiele do jednego
+----------------+       +-------------------+
|    Zamówienie  |       |     Klient        |
+----------------+       +-------------------+
| ZamówienieID (PK)|     | KlientID (PK)     |
| KlientID (FK)  |<------|                   |
| Produkt         |       |                   |
| Data            |       |                   |
+----------------+       +-------------------+

'''