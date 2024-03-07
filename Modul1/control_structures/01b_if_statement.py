
# ---------------------- Instrukcja if ---------------------- #
# ---------------------- Przykład 1: Proste polecenie if ---------------------- #
'''
Mamy zmienną wiek przypisaną wartość 25.
Instrukcja if sprawdza, czy wiek jest większy lub równy 18.
Jeśli warunek jest prawdziwy, drukuje "Jesteś uprawniony do głosowania". W przeciwnym razie drukuje "Nie jesteś uprawniony do głosowania."
'''
wiek = 25

# if wiek >= 18:
#     print("Jesteś uprawniony do głosowania.")
# else:
#     print("Nie jesteś uprawniony do głosowania.")



# ---------------------- Przykład 2: Instrukcja if-elif-else ---------------------- #
'''
Mamy zmienną wynik przypisaną wartość 85.
Instrukcja if-elif-else sprawdza wartość wynik w różnych przedziałach.
W zależności od przedziału przypisuje odpowiednią ocenę do zmiennej ocena.
Następnie drukuje ostateczną ocenę.

'''
# wynik = 85

# if wynik >= 90:
#     ocena = "A"
# elif wynik >= 80:
#     ocena = "B"
# elif wynik >= 70:
#     ocena = "C"
# elif wynik >= 60:
#     ocena = "D"
# else:
#     ocena = "F"

# print(f"Twoja ocena to {ocena}.")


# ---------------------- Przykład 3: Zagnieżdżone instrukcje if ---------------------- #
'''
Zewnętrzna instrukcja if sprawdza, czy liczba jest większa niż 0.
Jeśli warunek jest prawdziwy, przechodzi do zagnieżdżonego bloku if-else, sprawdzając, czy liczba jest parzysta czy nieparzysta.
Drukuje odpowiednią wiadomość na podstawie warunków.
'''

liczba = 12

# if liczba > 0:
#     if liczba % 2 == 0:
#         print("Liczba jest dodatnia i parzysta.")
#         if liczba > 10:
#             print("Liczba jest większa niż 10.")
#     else:
#         print("Liczba jest dodatnia i nieparzysta.")
# else:
#     print("Liczba nie jest dodatnia.")


# ---------------------- Przykład 4: Wiele warunków w jednej instrukcji if ---------------------- #
'''
Instrukcja if sprawdza dwa warunki za pomocą operatorów logicznych AND (and) i OR (or).
Drukuje wiadomość w zależności od tego, czy oba warunki są prawdziwe, przynajmniej jeden jest prawdziwy, czy żaden nie jest prawdziwy.
'''
x = 5
y = 0


# if x > 0 and y > 0:
#     print("Zarówno x, jak i y są dodatnie.")
# elif x > 0 or y > 0:
#     print("Przynajmniej jedno z x lub y jest dodatnie.")
# else:
#     print("Ani x, ani y nie jest dodatnie.")


# ---------------------- Przykład 5: Sprawdzanie przynależności za pomocą słowa kluczowego 'in' ---------------------- #
'''
Instrukcja if sprawdza, czy wybrane_owoc jest obecny na liście owoce za pomocą słowa kluczowego in.
Drukuje wiadomość w zależności od tego, czy owoc znajduje się na liście czy nie.

'''
owoce = ['jabłko', 'banan', 'pomarańcza']
wybrane_owoc = 'Jabłko'
# print(wybrane_owoc)
# wybrane_owoc = wybrane_owoc.upper()
# print(wybrane_owoc)

# Zwraca ostatni element listy
# print(owoce[-1])

# Zwraca pierwszy element listy
# print(owoce[0])

# if wybrane_owoc in owoce:
#     print(f"{wybrane_owoc} znajduje się na liście owoców.")
# else:
#     print(f"{wybrane_owoc} nie znajduje się na liście owoców.")


# ---------------------- Operatory relacji ---------------------- #

# ---------------------- Operator relacji: < ---------------------- #
'''
Sprawdzamy, czy Długość1 jest mniejsza niż Długość2.
'''
length1 = 8
length2 = 12

# if length1 < length2:
#     print(f"Długość1 ({length1}) jest mniejsza niż Długość2 ({length2}).")
# else:
#     print(f"Długość1 ({length1}) nie jest mniejsza niż Długość2 ({length2}).")


# ---------------------- Operator relacji: <= ---------------------- #
'''
Sprawdzamy, czy Ilość1 jest mniejsza lub równa Ilość2.
'''
quantity1 = 20
quantity2 = 20

# if quantity1 <= quantity2:
#     print(f"Ilość1 ({quantity1}) jest mniejsza lub równa Ilość2 ({quantity2}).")
# else:
#     print(f"Ilość1 ({quantity1}) nie jest mniejsza lub równa Ilość2 ({quantity2}).")


# ---------------------- Operator relacji: > ---------------------- #
'''
Sprawdzamy, czy Cena1 jest większa niż Cena2.
'''
price1 = 50
price2 = 30

# if price1 > price2:
    # print(f"Cena1 ({price1}) jest większa niż Cena2 ({price2}).")
# else:
    # print(f"Cena1 ({price1}) nie jest większa niż Cena2 ({price2}).")


# ---------------------- Operator relacji: >= ---------------------- #
'''
Sprawdzamy, czy Temperatura1 jest większa lub równa Temperatura2.
'''
temperature1 = 28
temperature2 = 28

# if temperature1 >= temperature2:
    # print(f"Temperatura1 ({temperature1}) jest większa lub równa Temperatura2 ({temperature2}).")
# else:
    # print(f"Temperatura1 ({temperature1}) nie jest większa lub równa Temperatura2 ({temperature2}).")


# ---------------------- Operator relacji: == ---------------------- #
'''
Sprawdzamy, czy Ocena1 jest równa Ocena2.
'''
marks1 = 90
marks2 = 90

# if marks1 == marks2:
#     print(f"Ocena1 ({marks1}) jest równa Ocena2 ({marks2}).")
# else:
#     print(f"Ocena1 ({marks1}) nie jest równa Ocena2 ({marks2}).")


# ---------------------- Operator relacji: != ---------------------- #
'''
Sprawdzamy, czy Prędkość1 jest różna od Prędkość2.
'''
speed1 = 120
speed2 = 100

# if speed1 != speed2:
    # print(f"Prędkość1 ({speed1}) nie jest równa Prędkość2 ({speed2}).")
# else:
    # print(f"Prędkość1 ({speed1}) jest równa Prędkość2 ({speed2}).")


# ---------------------- Zasady ewaluacji do bool ---------------------- #
'''
Wartości Prawdziwe (True):
Wartość True sama w sobie jest prawdziwa.
Wartość różna od zera, np. liczby różne od zera, niepuste ciągi znaków, listy, itp., jest traktowana jako prawda.
Niepusty obiekt, taki jak niepusta lista czy niepusty string, jest ewaluowany jako prawda.
Wartości Fałszywe (False):

Wartość False sama w sobie jest fałszywa.
Wartość zero, np. 0 dla int, 0.0 dla float, jest traktowana jako fałsz.
Pusty obiekt, taki jak pusty string czy pusta lista, jest ewaluowany jako fałsz.
'''
# Przykład 1: Wartość True
bool_value = bool(True)
# print(bool_value)  # True

# Przykład 2: Wartość False (0)
bool_value = bool(0)
# print(bool_value)  # False

# Przykład 3: Wartość False (pusty string)
bool_value = bool('')
# print(bool_value)

# Przykład 4: Wartość True (niepusty string)
bool_value = bool('Hello')
# print(bool_value)  # True

# Przykład 5: Wartość False (pusta lista)
bool_value = bool(['test'])
# print(bool_value)  # False

# Przykład 6: Wartość True (liczba różna od zera)
bool_value = bool(42)
# print(bool_value)  # True

# Przykład 7: Wartość False (pusta krotka)
bool_value = bool(())
# print(bool_value)  # False

# Przykład 8: Wartość True (niepusty słownik)
bool_value = bool({})
# print(bool_value)  # True

# Przykład 9: Wartość False (zero jako float)
bool_value = bool(0.0)
# print(bool_value)  # False

# Przykład 10: Wartość True (niepusty zbiór)
bool_value = bool({1, 2, 3})
# print(bool_value)  # True


# ---------------------- Algebra Boole'a ---------------------- #

# ---------------------- Operator logiczny: and ---------------------- #
# Przykład 1
x = True
y = True
result1 = x and y
# print(result1)  # True

# Przykład 2
a = True
b = False
result2 = a and b
# print(result2)  # False


# ---------------------- Operator logiczny: or ---------------------- #
# Przykład 3
p = False
q = True
result3 = p or q
# print(result3)  # True

# Przykład 4
m = False
n = False
result4 = m or n
# print(result4)  # False


# ---------------------- Operator logiczny: not ---------------------- #
# Przykład 5
flag1 = True
result5 = not flag1
# print(result5)  # False

# Przykład 6
flag2 = False
result6 = not flag2
# print(result6)  # True

# print(3 + 4 <= 3 == True) # False True


# ---------------------- Instrukcje warunkowe zagnieżdżone ---------------------- #

# ---------------------- Przykład 1 ---------------------- #
x = 10
y = 1

# if x > 5:
#     print("x jest większe niż 5")
    
#     if y > 2:
#         print("y jest większe niż 2")
#     else:
#         print("y nie jest większe niż 2")

# else:
#     print("x nie jest większe niż 5")



# ---------------------- Przykład 2 ---------------------- #
# grade = 85

# if grade > 95:
#     print("Ocena: A+")
# elif grade >= 90:
#     print("Ocena: A")
# elif grade >= 80:
#     print("Ocena: B")
    
#     if grade >= 85:
#         print("Jest to jednak B+")
#     else:
#         print("To jest zwykłe B")

# elif grade >= 70:
#     print("Ocena: C")
# else:
#     print("Ocena: F")

print((4 > 3) == True)
