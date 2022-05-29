import logging
logging.basicConfig(level=logging.INFO)

'''
Prosty kalkulator który pozwala wykonywać działania na dwóch liczbach.
'''

def calculation_choice(number): #Funkcja która wykonuje odpowiednie działanie w zależności od wyboru opcji użytkownika
    if number == 1:
        logging.info(f'Dodaję {first_number} do {second_number}')
        print(first_number + second_number)
    elif number == 2:
        logging.info(f'Odejmuję {first_number} od {second_number}')
        print(first_number - second_number)
    elif number == 3:
        logging.info(f'Mnożę {first_number} razy {second_number}')
        print(first_number * second_number)
    elif number == 4:
        logging.info(f'Dzielę {first_number} przez {second_number}')
        print(first_number / second_number)

def choose_again(number): #Funkcja która pozwala na ponowny wybór opcji działania w przypadku wpisania innej liczby niż od 1 do 4

    while number < 1 or number > 4:

        try: #Pętla która wypisuje treść błędu dopóki wpisane dane nie będą odpowiadać wymaganym (float)
            logging.warning('Wybór nie odpowiada opcją. Dokonaj wyboru ponownie: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
            number = int(input())
        except ValueError:
            print('Wybór nie jest liczbą, spróbuj ponownie')

    return number

if __name__ == '__main__':

    print('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')

    while True:
        try:
            choice_number = int(input()) #Wybór opcji działania
            break;
        except ValueError:
            print('Wybór nie jest liczbą, spróbuj ponownie')
            
    choice_number = choose_again(choice_number)

    while True: #Pętla która wypisuje treść błędu dopóki wpisane dane nie będą odpowiadać wymaganym (float)
        try:
            first_number = float(input('Podaj pierwszą liczbę: '))
            break;
        except ValueError:
            print('Dane nie jest liczbą, spróbuj ponownie')

    while True: #Pętla która wypisuje treść błędu dopóki wpisane dane nie będą odpowiadać wymaganym (float)
        try:
            second_number = float(input('Podaj drugą liczbę: '))
            break;
        except ValueError:
            print('Dane nie jest liczbą, spróbuj ponownie')

    print('Wynik dodawania to:')
    calculation_choice(choice_number)
    