from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    diff = randint(1, 5)
    first = randint(1, 5)
    last = first + (9 * diff)
    progression = list(range(first, last + 1, diff))
    index = randint(0, 9)
    answer = str(progression[index])
    progression[index] = '..'
    question = f'{" ".join(map(str, progression))}'
    return answer, question
