import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    return print(f'Hello, {name}!')
