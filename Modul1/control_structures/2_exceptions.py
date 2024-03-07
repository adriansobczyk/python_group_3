# ---------------------- Przykłady błędów ---------------------- #

# ---------------------- SyntaxError ---------------------- #
# SyntaxError: Niepoprawne użycie cudzysłowów
# x = "hello'
# print(x)

# ---------------------- IndentationError ---------------------- #
# IndentationError: Nieprawidłowy wcięcia - mieszane tabulatory i spacje
# x = 2
# if x > 0:
#     print("x jest dodatnie.")

# ---------------------- TabError ---------------------- #
# TabError: Niespójne użycie tabulatorów i spacji
# x = 5
# if x > 0:
#     print("x jest dodatnie.")
#         print("x jest większe od 0.")

# ---------------------- TypeError ---------------------- #
# TypeError: Nieprawidłowe działanie na typie danych
# x = 10 + "20"
# print(x)

# ---------------------- ValueError ---------------------- #
# ValueError: Nieprawidłowa konwersja napisu na liczbę
# x = int("abc")
# print(x)

# ---------------------- ZeroDivisionError ---------------------- #

# ZeroDivisionError: Dzielenie przez zero
# x = 5 / 0
# print(x)

# ---------------------- FileNotFoundError ---------------------- #
# FileNotFoundError: Brak pliku
# with open("test.txt") as f:
#     print(f.read())

# ---------------------- IndexError ---------------------- #

# IndexError: Przekroczenie zakresu listy
# numbers = [1, 2, 3]
# print(numbers[3])

# ---------------------- KeyError ---------------------- #
# # KeyError: Brak klucza w słowniku
# person = {
#     "name": "John",
#     "age": 36
# }
# print(person["address"])


# num = 7

# try:
#     if num > 5:
#         print(f"{num} jest większa niż 5.")
#     elif num < 5:
#         print(f"{num} jest mniejsza niż 5.")
#     else:
#         print(f"{num} jest równa 5.")
# except Exception as error_msg:
#     print(error_msg)
#     print(f"Nie można porównać {num} z liczbą 5.")
# finally:
#     print("To jest blok 'finally'.")


# ---------------------- Obsługa wyjątków w pętlach ---------------------- #

# numbers = [1, 2, 0, '6', 5]

# for num in numbers:
    # if num == 0:
    #     print("Nie można dzielić przez 0!")
    #     continue
    # try:
    #     result = 10 / num
    #     print(f"10 / {num} = {result}")
    # except ZeroDivisionError as e:
    #     # print(f"Wystąpił błąd: {e}")
    #     print(f"Nie można dzielić przez 0! Opuszczam {num}")
    # except TypeError as e:
    #     # print(f"Wystąpił błąd: {e}")
    #     print(f"Zły typ danych! Opuszczam {num}")
    # except Exception as e:
    #     print(f"Wystąpił nieoczekiwany błąd: {e}")



# ---------------------- Obsługa wyjątków w pętlach ---------------------- #

# while True:
#     try:
#         user_input = input("Wprowadź liczbę (lub 'exit' aby zakończyć): ")
        
#         if user_input.lower() == 'exit':
#             print("Zakończono program.")
#             break  # Zakończ pętlę, jeśli użytkownik wpisze 'exit'

#         num = float(user_input)
#         result = 10 / num
#         print(f"10 / {num} = {result}")

#     except ValueError:
#         print("To nie jest poprawna liczba. Spróbuj ponownie.")
#     except ZeroDivisionError:
#         print("Nie można dzielić przez zero. Spróbuj ponownie.")
#     except Exception as e:
#         print(f"Wystąpił nieoczekiwany błąd: {e}")


# Pętle for i while z obsługą wyjątków
# while True:
#     try:
#         user_input = input("Wprowadź liczbę (lub 'exit' aby zakończyć): ")
        
#         if user_input.lower() == 'exit':
#             print("Zakończono program.")
#             break  # Zakończ program, jeśli użytkownik wpisze 'exit'

#         num = float(user_input)
        
#         # Pętla for - iteracja przez wprowadzoną liczbę
#         print("Iteracja przez liczbę przy użyciu pętli for:")
#         for i in range(int(num)):
#             print(i)

#         # Pętla while - powtarzaj dopóki liczba nie osiągnie 0
#         print("Pętla while - odliczanie od wprowadzonej liczby do zera:")
#         while num >= 0:
#             print(num)
#             num = num - 1

#     except ValueError:
#         print("To nie jest poprawna liczba. Spróbuj ponownie.")
#     except ZeroDivisionError:
#         print("Nie można dzielić przez zero. Spróbuj ponownie.")
#     except Exception as e:
#         print(f"Wystąpił nieoczekiwany błąd: {e}")


# Przykład pętli while z pętlą for wewnątrz i obsługą wyjątków
# counter_outer = 0
# while counter_outer < 3:
#     print(f"Iteracja zewnętrzna: {counter_outer}")
    
#     try:
#         # Pętla for wewnątrz pętli while
#         fruits = ["jabłko", "banan", "gruszka"]
#         for i in range(len(fruits) + 1):  # Przekroczenie zakresu listy, aby wywołać IndexError
#             print(f"    Owoc: {fruits[i]}")
    
#     except IndexError as e:
#         print(f"    Błąd indeksu: {e}. Pętla for przerwana.")
    
#     counter_outer += 1


# Przykład pętli for z pętlą while wewnątrz i obsługą wyjątków
# fruits = ["jabłko", "banan", "gruszka"]
# for fruit in fruits:
#     print(f"Owoc: {fruit}")

#     counter = 0
#     try:
#         while counter < 4:
#             print(f"    Iteracja wewnętrzna: {counter}")
#             # Symulacja błędu indeksu
#             fruit_to_print = fruits[counter + 1]  # To spowoduje IndexError
#             counter += 1

#     except IndexError as e:
#         print(f"    Błąd indeksu: {e}. Pętla while przerwana.")

# print("Koniec programu.")
