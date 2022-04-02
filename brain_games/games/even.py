from random import randint
import prompt


def test():
    random_number = randint(1, 100)
    truth = 'yes' if random_number % 2 == 0 else 'no'
    print(f'Question: {random_number}')
    bet = prompt.string('Your answer: ')
    return bet, truth


def main(name, iterator):
    if iterator > 2:
        return print(f'Congratulations, {name}!')
    else:
        outcome = test()
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
