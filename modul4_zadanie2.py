import logging



def calculation_choice(number):
    if number == 1:
        print(first_number + second_number)
    elif number == 2:
        print(first_number - second_number)
    elif number == 3:
        print(first_number * second_number)
    elif number == 4:
        print(first_number / second_number)

def choose_again(number):
  while number < 1 or number > 4:
    print('Wybór nie odpowiada opcją. Dokonaj wyboru jeszcze raz: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
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