import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    number_of_trials = 3
    for i in range(number_of_trials):
        truth = game.get_question_and_answer()
        bet = prompt.string('Your answer: ')
        if bet == truth:
            print('Correct!')
        else:
            print(f"'{bet}' is wrong answer ;(. Correct answer was '{truth}'.")
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
