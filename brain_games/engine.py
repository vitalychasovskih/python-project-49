from brain_games.cli import welcom_user
from brain_games.constants import NUMBER_OF_ROUNDS


def brain_engine(game):
    print('Welcome to the Brain Games!')
    name = welcom_user()
    print(game.description)
    counter = 0
    flag = True
    while counter < NUMBER_OF_ROUNDS:
        question, perfect_answer = game.logic()
        print('Question: ', question)
        answer = input('Your answer: ')
        if answer == perfect_answer:
            print("Correct!")
            counter += 1
        else:
            flag = False
            lost_message = (
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{perfect_answer}'."
            )
            print(lost_message)
            print(f"Let's try again, {name}!")
            break
    if flag:
        print(f"Congratulations, {name}!")
