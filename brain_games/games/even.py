from random import randint
import prompt


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def test():
    random_number = randint(1, 100)
    truth = 'yes' if random_number % 2 == 0 else 'no'
    print(f'Question: {random_number}')
    bet = prompt.string('Your answer: ')
    return bet, truth
