import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    rand_num1 = random.randint(1, 100)
    rand_num2 = random.randint(1, 100)
    m = random.choice(list(operations.keys()))
    result = operations[m](rand_num1, rand_num2)
    question = f'{rand_num1} {m} {rand_num2}'
    correct_answer = str(result)
    return correct_answer, question
