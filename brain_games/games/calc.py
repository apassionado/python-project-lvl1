import random
import operator


DESCRIPTION = 'What is the result of the expression?'

ops_sequence = random.sample(['+', '-', '*'], 3)
# global variable is for each test consisted of 3 unique ops


def get_question_and_answer():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    rand_num1 = random.randint(1, 100)
    rand_num2 = random.randint(1, 100)
    m = ops_sequence.pop(0)
    result = operations[m](rand_num1, rand_num2)
    question = f'{rand_num1} {m} {rand_num2}'
    return str(result), question
