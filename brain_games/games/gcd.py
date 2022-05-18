from random import randint
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    rand_num1 = randint(1, 100)
    rand_num2 = randint(1, 100)
    result = math.gcd(rand_num1, rand_num2)
    correct_answer = str(result)
    question = f'{rand_num1} {rand_num2}'
    return correct_answer, question
