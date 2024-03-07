# ---------------------- Pętle ---------------------- #

# ---------------------- Pętla for ---------------------- #

# Składnia
# for zmienna_iteracyjna in kolekcja:
#     blok kodu
# Przykłady

# ---------------------- Przykład 1: Prosta pętla for ---------------------- #
'''
Prosta pętla for - wypisanie liczb od 0 do 9
'''
# for num in range(10):
#     num = num + 1
#     print(num)

# ---------------------- Przykład 2: Pętla for z listą ---------------------- #
'''
Pętla for z listą - wypisanie liczb od 0 do 9
'''

# lista = [-1, 0, 1, 2, 3, 4, 5]

# for element in lista:
#     print(element)

# ---------------------- Przykład 3: Pętla for ze słownikiem ---------------------- #
'''
Pętla for ze słownikiem - wypisanie kluczy, wartości i par klucz-wartość
'''
# sample_dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4
# }

# for sample_dict_key in sample_dict:
#     print(sample_dict_key)

# for sample_dict_key in sample_dict.values():
#     print(sample_dict_key)

# for key, value in sample_dict.items():
#     # print(key, value)
#     print(f"Klucz: {key}, wartość: {value}")


# ---------------------- Przykład 4: Pętla for z krotką ---------------------- #
'''
Pętla for z krotką - wypisanie liczb od 0 do 9
'''
# krotka = (1, 2, 3, 4, 5)

# for element in krotka:
#     print(element)

# sample_str = ['a', 2, 'c', 'd']

# for char in sample_str:
#     print(char)
# sample_list = ['a', 2, 'c', 'd']
# sample_tuple = ('a', 2, 'c', 'd')
# sample_tuple.pop(0)
# print(sample_tuple)

# ---------------------- Przykład 5: Pętla for z zagnieżdżonymi kolekcjami ---------------------- #
'''
Pętla for z zagnieżdżonymi kolekcjami - wypisanie liczb od 0 do 9
'''
# sample_list = ['a', 2, 'c', 'd']
# sample_list2 = ['a', 2, 'c', 'd']
# sample_list3 = ['a', 2, 'c', 'd']

# concatenated_list = sample_list + sample_list2 + sample_list3
# print(type(concatenated_list))
# lista = [
#     sample_list,
#     sample_list2,
#     sample_list3
# ]

# for element in lista:
#     print(element)

# for element in lista:
    #  Iteracja przez elementy wewnętrznej listy
    # for item in element:
        # print(item)

# print(type(lista))

# ---------------------- Przykład 6: Pętla for z zagnieżdżonymi kolekcjami ---------------------- #
'''
Pętla for z zagnieżdżonymi kolekcjami - wypisanie liczb od 0 do 9
'''

# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# ---------------------- Pętla while ---------------------- #
'''
Pętla while - wypisanie liczb od 0 do 9
'''

# Składnia
# while warunek:
#     blok kodu

# ---------------------- Prosta pętla while ---------------------- #
'''
Prosta pętla while - wypisanie liczb od 0 do 9
'''

# num = 0
# while num <= 10:
#     print(num)
#     num += 1

# ---------------------- Pętla while z instrukcją break ---------------------- #
'''
Pętla while z break - przerwanie pętli przy i == 5
'''

# number = int(input("Wprowadź liczbę: "))
# while True:
#     print(number)
#     number -= 1
#     if number < 0:
#         break  # Przerwanie zewnętrznej pętli, gdy number < 0


# ---------------------- Pętla while z instrukcją continue ---------------------- #
'''
Pętla while z continue - pominięcie liczb parzystych
'''

# k = 0
# while k < 9:
#     k += 1
#     if not k % 2:
#         continue
#     print(k)

# TRUE, FALSE, TRUE, FALSE, TURE, FALSE

# ---------------------- Pętla while z instrukcją continue oraz break ---------------------- #
'''
Pętla while z continue i break - pominięcie liczb parzystych i przerwanie przy a > 5
'''

# a = 0
# while a < 10:
#     a += 1
#     if not a % 2:
#         continue  # Pominięcie liczb parzystych, przejście do następnej iteracji
#     print(a)
#     if a >= 5:
#         break  # Przerwanie pętli, gdy a > 5

# ---------------------- Pętla while z else ---------------------- #
'''
Pętla while z else - wypisanie liczb od 0 do 9
'''

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print('Koniec pętli')

# ---------------------- Zagnieżdżona pętla while ---------------------- #
'''
Zagnieżdżona pętla while - wypisanie liczb od 0 do 9
'''

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break


# ---------------------- Nieskończona pętla while ---------------------- #
'''
Niekończąca się pętla while - wypisanie liczb od 0 do nieskończoności
'''

# a = 0
# while True:
#     print(a)
    # a += 1


# ---------------------- Nieskończona pętla for ---------------------- #
'''
Niekończąca się pętla for - wypisanie liczb od 0 do nieskończoności
'''

# x = [1]
# for i in x:
#     x.append(i+1)
#     print(i)


# ---------------------- Przykład pętli while z pętlą for wewnątrz ---------------------- #
'''
Pętla while z pętlą for wewnątrz - wypisanie owoców z listy 3 razy
'''

# counter_outer = 0
# while counter_outer < 3:
#     print(f"Iteracja zewnętrzna: {counter_outer}")
    
#     # Pętla for wewnątrz pętli while
#     fruits = ["jabłko", "banan", "gruszka"]
#     for fruit in fruits:
#         print(f"    Owoc: {fruit}")
    
#     counter_outer += 1


# ---------------------- Przykład pętli for z pętlą while wewnątrz ---------------------- #
'''
Pętla for z pętlą while wewnątrz - wypisanie owoców z listy 3 razy
'''

# fruits = ["jabłko", "banan", "gruszka"]
# for fruit in fruits:
#     print(f"Owoc: {fruit}")

#     counter = 0
#     while counter < 5:
#         print(f"    Iteracja wewnętrzna: {counter}")
#         counter += 1



# ---------------------- Ord oraz char ---------------------- #

# Funkcja ord przyjmuje pojedynczy znak jako argument i zwraca jego kod Unicode.
# print(ord('a'))

# Funkcja chr przyjmuje liczbę całkowitą (kod Unicode) i zwraca odpowiadający mu znak.
# print(chr(65))

# Pętla for - iteracja przez zakres kodów Unicode
# for i in range(65, 65+26):
#     print(chr(i), end = " , ")

# y = ord('A')
# print(type(y), y)
 
 # Przypisanie kodu Unicode do zmiennej
# alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Print 65-90
# for i in alphabet_list:
#     print(ord(i), end = " , ")