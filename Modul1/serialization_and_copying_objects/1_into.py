'''
1. Serializacja oraz deserializacja danych - co to jest?
'''

# Przykład 1 
# serializacja danych do pliku
expenses = {
    "hotel": 150,
    "breakfast": 30,
    "taxi": 15,
    "lunch": 20
}

# file_name = "1_expenses.txt"
# with open(file_name, "w") as fh:
#     for key, value in expenses.items():
#         fh.write(f"{key}|{value}\n")


# deserializacja danych z pliku
# file_name = "1_expenses.txt"
# expenses = {}

# with open(file_name, "r") as fh:
#     raw_expenses = fh.readlines()
#     for line in raw_expenses:
#         key, value = line.strip().split("|")
#         expenses[key] = str(value)
# print(expenses)


# Przykład 2
# serializacja danych do pliku
# sample_text = "This is Lorem Ipsum sample text."
# file_name = "1_text.txt"
# with open(file_name, "w") as file:
#     file.write(sample_text)
# deserializacja danych z pliku
# file_name = "1_text.txt"
# with open(file_name, "r") as file:
#     sample_text = file.read()
#     print(sample_text)