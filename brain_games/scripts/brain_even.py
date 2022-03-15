#!/usr/bin/env python
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for i in range(3):
        random_number = randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print(f'Question: {random_number}!')
        ev_chk = 'no'
        if random_number % 2 == 0:
            ev_chk = 'yes'
        bet = prompt.string('Your answer: ')
        if bet == ev_chk:
            print('Correct!')
        else:
            print(f"'{bet}' is wrong answer ;(. Correct answer was '{ev_chk}'.")
            print(f"Let's try again, {name}!")
            return  # перевод каретки внутри print? \n
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
