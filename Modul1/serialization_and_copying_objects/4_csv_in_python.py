'''
4. Praca z tabelami CSV w Pythonie
'''
import csv

# 1. Zapisanie pliku CSV
# with open('4_data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['first_name', 'last_name', 'email'])
#     writer.writerow(['John', 'Doe', 'j.doe@gmail.com'])


# # 2. Odczytanie pliku CSV
# with open('4_data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# # 3. DictWriter - zapisanie pliku CSV jako słownik
# with open('4_data_dict.csv', 'a', newline='') as file:
#     fieldnames = ['first_name', 'last_name', 'email']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'first_name': 'John', 'last_name': 'Doe', 'email': 'j.doe@gmail.com'})

# # 4. DictReader - odczytanie pliku CSV jako słownik
# with open('4_data_dict.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['first_name'], row['last_name'], row['email'])
