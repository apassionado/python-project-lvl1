from random import randint
import prompt
# import math


def loop(last):
    truth = 'yes'
    for i in range(2, last):
        if last % i == 0:
            truth = 'no'
    return truth


def test():
    last = randint(2, 100)
    truth = loop(last)
    print(f'Question:{last}')
    bet = prompt.string('Your answer: ')
    return bet, truth


def main(name, iterator):
    if iterator > 2:
        return print(f'Congratulations, {name}!')
    else:
        outcome = test()
        bet = outcome[0]
        truth = outcome[1]
        if bet == truth:
            print('Correct!')
            iterator += 1
            main(name, iterator)
        else:
            print(f"'{bet}' is wrong answer ;(. Correct answer was '{truth}'.")
            print(f"Let's try again, {name}!")
            return
    return
