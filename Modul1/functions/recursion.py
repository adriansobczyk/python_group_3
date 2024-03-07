# ---------------------- Rekursja ---------------------- #

# Rekursja to technika programowania, w której funkcja wywołuje samą siebie. 
# Często używana do rozwiązywania problemów, które można podzielić na podproblemy o tej samej strukturze.

def suma_for(liczba):
    '''
    Funkcja zwraca sumę liczb od 0 do liczba.
    '''
    suma = 0
    for i in range(liczba + 1):
        suma += i

    return suma

# print(suma_for(7))


def sum_for_recursion(liczba):
    '''
    Funkcja zwraca sumę liczb od 0 do liczba
    Warunek bazowy (n == 0 or n == 1) zatrzymuje rekurencję, gdy n osiąga wartość 0 lub 1, zwracając wtedy 1.
    '''
    if liczba == 0: return 0
    return liczba + sum_for_recursion(liczba - 1)

# print(sum_for_recursion(7))


def fibonacci_recursive(n):
    if n in [0, 1]:
        # print(f"fibonacci_recursive({n}) = {n}")
        return n
    result = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    # print(f"fibonacci_recursive({n}) = {result}")
    return result

# Przykład użycia
# n = 15 # Liczba elementów ciągu Fibonacciego do wygenerowania, uważaj przy wartościach > 30 ze względu na wydajność algorytmu. O tym jak to zoptymalizować dowiesz się w kolejnych lekcjach.
# result = fibonacci_recursive(n)
# print(f"Pierwsze {n} elementy ciągu Fibonacciego: {result}")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# # Przykład użycia
# number = 5
# result = factorial(number)
# print(f"Silnia z {number} to {result}")

# ---------------------- Przykład graficzny rekurencji ---------------------- #
# import turtle

# t = turtle.Turtle()
# t.speed(-1)
# t.setheading(90)
# t.penup()
# t.goto(0,-200)
# t.pendown()

# def gałąź(t, len):

#     if len == 0: return

#     nt = t.clone()
#     nt.forward(50)

#     nt.left(20)
#     gałąź(nt,len-1)

#     nt.right(40)
#     gałąź(nt,len-1)
    
# gałąź(t, 7)
# window = turtle.Screen()
# window.exitonclick()