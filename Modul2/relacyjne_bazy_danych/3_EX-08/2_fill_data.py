from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_COMPANIES = 3
NUMBER_EMPLOYESS = 30
NUMBER_POST = 5

def generate_fake_data(number_companies, number_employees, number_post) -> tuple():
    fake_companies = []# tu będą przechowywane firmy
    fake_employees = []# tu będą przechowywane pracownicy
    fake_posts = []# tu będą przechowywane stanowiska
    '''Weźmy trzy firmy z Fakera i umieśćmy je w odpowiedniej zmiennej'''
    fake_data = faker.Faker()

# Tworzymy tyle firm: number_companies
    for _ in range(number_companies):
        fake_companies.append(fake_data.company())

# Generujemy tyle pracowników: number_employees'''
    for _ in range(number_employees):
        fake_employees.append(fake_data.name())

# Oraz tyle stanowisk: number_post
    for _ in range(number_post):
        fake_posts.append(fake_data.job())

    return fake_companies, fake_employees, fake_posts


def prepare_data(companies, employees, posts) -> tuple():
    for_companies = []
    # przygotowanie listy krotek z nazwami firm
    for company in companies:
        for_companies.append((company, ))

    for_employees = []# dla tabeli employees

    for emp in employees:
        '''
        Aby wprowadzić dane do tabeli pracowników, musimy dodać stanowisko i identyfikator firmy. Domyślnie mieliśmy tyle firm:
        NUMBER_COMPANIES. Podczas tworzenia tabeli companies zaznaczyliśmy, że wartości w kolumnie id będą INTEGER AUTOINCREMENT - czyli
        każdy rekord będzie miał przypisany kolejny numer zwiększony o 1, zaczynając od 1. Dlatego firma jest
        wybierana losowo w dostępnym przedziale liczbowym.
        '''
        for_employees.append((emp, choice(posts), randint(1, NUMBER_COMPANIES)))

    '''
     Podobne operacje wykonamy w tabeli payments z wynagrodzeniami. Załóżmy, że wypłaty wynagrodzeń we wszystkich firmach
    odbywały się od 10 do 20 dnia każdego miesiąca. Wygenerujemy widełki wynagrodzeń w zakresie od 1000 do 10000 jednostek jakiejś waluty
    w każdym miesiącu i w przypadku każdego pracownika.
    '''
    for_payments = []

    for month in range(1, 12 + 1):
        # Pętla po miesiącach'''
        payment_date = datetime(2021, month, randint(10, 20)).date()
        for emp in range(1, NUMBER_EMPLOYESS + 1):
        # Pętla po pracownikach
            for_payments.append((emp, payment_date, randint(1000, 10000)))

    return for_companies, for_employees, for_payments

def insert_data_to_db(companies, employees, payments) -> None:
# Tworzenie połączenia z bazą danych i pobieranie obiektu kursora do manipulowania danymi.

    with sqlite3.connect('salary.db') as con:

        cur = con.cursor()

        '''Wypełniamy tabelę firm. Tworzymy skrypt do wstawienia, w którym oznaczamy zmienne do wstawienia za pomocą
znaku zastępczego (?) '''

        sql_to_companies = """INSERT INTO companies(company_name)
                               VALUES (?)"""

        '''Aby wstawić wszystkie dane naraz,  używamy metody executemany kursora. Pierwszym parametrem będzie tekst
        skryptu, a drugim dane (lista krotek).'''

        cur.executemany(sql_to_companies, companies)

# Następnie wstawiamy dane pracowników. Napiszmy w tym celu skrypt i określmy zmienne
        sql_to_employees = """INSERT INTO employees(employee, post, company_id)
                               VALUES (?, ?, ?)"""

# Dane zostały przygotowane wcześniej, więc po prostu przekazujemy je do funkcji

        cur.executemany(sql_to_employees, employees)

# Na koniec wypełniamy tabelę kwotami wynagrodzeń

        sql_to_payments = """INSERT INTO payments(employee_id, date_of, total)
                              VALUES (?, ?, ?)"""

# Wstawiamy dane dotyczące wynagrodzenia

        cur.executemany(sql_to_payments, payments)

# Zapisujemy zmiany w bazie danych

        con.commit()

if __name__ == "__main__":
    companies, employees, posts = prepare_data(*generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYESS, NUMBER_POST))
    print(companies)    
    print(employees)
    print(posts)
    insert_data_to_db(companies, employees, posts)
