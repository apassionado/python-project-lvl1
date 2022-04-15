from random import randint
import prompt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def loop(last):
    truth = 'yes'
    for i in range(2, last):
        if last % i == 0:
            truth = 'no'
    return truth


def test():
    last = randint(2, 100)
    truth = loop(last)
    print(f'Question: {last}')
    bet = prompt.string('Your answer: ')
    return bet, truth
