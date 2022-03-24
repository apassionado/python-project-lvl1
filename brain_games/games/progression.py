from random import randint
import prompt
# import math


def sequence():
    diff = randint(1, 5)
    first = randint(1, 5)
    quise = first + (randint(0, 9) * diff)
    after_last = first + (10 * diff)
    test_string = ''
    a = ''
    for i in range(first, after_last, diff):
        a = '..' if i == quise else str(i)
        test_string = f'{test_string} {a}'
    return test_string, quise


def test(test_string, quise):
    print(f'Question:{test_string}')
    bet = prompt.string('Your answer: ')
    truth = str(quise)
    return bet, truth


def main(name, iterator):
    if iterator > 2:
        return print(f'Congratulations, {name}!')
    else:
        tuple_seq = sequence()
        outcome = test(tuple_seq[0], tuple_seq[1])
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
