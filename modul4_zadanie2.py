import logging
logging.basicConfig(level=logging.DEBUG)

'''
Prosty kalkulator który pozwala wykonywać działa na dwóch liczbach.
'''

def calculation_choice(number): #Funkcja która wykonuje odpowiednie działanie w zależności od wyboru użytkownika
    if number == 1:
        logging.debug(f'Dodaję {first_number} do {second_number}')
        print(first_number + second_number)
    elif number == 2:
        logging.debug(f'Odejmuję {first_number} od {second_number}')
        print(first_number - second_number)
    elif number == 3:
        logging.debug(f'Mnożę {first_number} razy {second_number}')
        print(first_number * second_number)
    elif number == 4:
        logging.debug(f'Dzielę {first_number} przez {second_number}')
        print(first_number / second_number)


def choose_again(number): #Funkcja która pozwala na ponowny wybór opcji działania w przypadku braku wybrania opcji od 1 do 4
  while number < 1 or number > 4:
    logging.warning('Wybór nie odpowiada opcją. Dokonaj wyboru ponownie: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
    number = int(input())
  return number

if __name__ == '__main__':

    print('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
    choice_number = int(input())
    choice_number = choose_again(choice_number)
    print('Podaj pierwszą liczbę:')
    first_number = int(input())
    print('Podaj drugą liczbę')
    second_number = int(input())
    print('Wynik dodawania to: ')
    calculation_choice(choice_number)