import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game):
    name = greet()
    print(game.DESCRIPTION)
    for i in range(3):
        outcome = game.test()
        bet = outcome[0]
        truth = outcome[1]
        if bet == truth:
            print('Correct!')
        else:
            print(f"'{bet}' is wrong answer ;(. Correct answer was '{truth}'.")
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
