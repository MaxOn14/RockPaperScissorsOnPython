import random


def game():
    choices = ['rock', 'paper', 'scissors']

    user_choice = None

    while user_choice not in choices:
        user_choice = input('Введите ваш выбор в игре камень ножницы бумага: ').lower().strip(' ')

    random_choice = random.choice(choices)

    if user_choice == random_choice:
        print('Ничья!', 'Выбор программы:', random_choice, 'Выбор пользователя:', user_choice)
    elif user_choice == 'rock' and random_choice == 'rock':
        print('Вы проиграли!', 'Выбор программы:', random_choice, 'Выбор пользователя:', user_choice)
    elif user_choice == 'paper' and random_choice == 'scissors':
        print('Вы проиграли!', 'Выбор программы:', random_choice, 'Выбор пользователя:', user_choice)
    elif user_choice == 'scissors' and random_choice == 'rock':
        print('Вы проиграли!', 'Выбор программы:', random_choice, 'Выбор пользователя:', user_choice)
    else:
        print('Вы победили!', 'Выбор программы:', random_choice, 'Выбор пользователя:', user_choice)
    restart_choices = ['y', 'n']
    y_n = None
    while y_n not in restart_choices:
        y_n = input('Do you want to restart? Y/N: ')
    if y_n == 'y':
        game()
    elif y_n == 'n':
        print('Game over')
        return

game()