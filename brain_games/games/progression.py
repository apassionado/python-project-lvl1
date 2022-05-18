from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    step = randint(1, 5)
    first = randint(1, 5)
    length = 10
    last = first + (length - 1) * step
    progression = list(range(first, last + 1, step))
    index = randint(0, 9)
    correct_answer = str(progression[index])
    progression[index] = '..'
    question = f'{" ".join(map(str, progression))}'
    return correct_answer, question
