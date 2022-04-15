from random import randint
import prompt
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def test():
    rand_num1 = randint(1, 100)
    rand_num2 = randint(1, 100)
    result = math.gcd(rand_num1, rand_num2)
    print(f'Question: {rand_num1} {rand_num2}')
    bet = prompt.string('Your answer: ')
    truth = str(result)
    return bet, truth
