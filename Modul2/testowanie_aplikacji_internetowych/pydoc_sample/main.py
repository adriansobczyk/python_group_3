"""
main - Przykładowy moduł demonstracyjny

Ten moduł zawiera przykładowe funkcje i klasy, które ilustrują,
jak działa dokumentowanie kodu przy użyciu pydoc.

pydoc main
pydoc -w main
pydoc -p 8080
"""

def example_function(x, y):
    """
    Oblicza sumę dwóch liczb.

    Args:
        x (int): Pierwsza liczba.
        y (int): Druga liczba.

    Returns:
        int: Suma liczb x i y.
    """
    return x + y

class ExampleClass:
    """
    Przykładowa klasa demonstracyjna.

    Ta klasa zawiera przykładową metodę, która zwraca powitanie.
    """

    def __init__(self, name):
        """
        Inicjalizuje obiekt ExampleClass.

        Args:
            name (str): Imię użytkownika.
        """
        self.name = name

    def greet(self):
        """
        Zwraca powitanie.

        Returns:
            str: Powitanie użytkownika.
        """
        return f"Hello, {self.name}!"
