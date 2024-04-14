from brain_games.cli import welcome_user


def brain_engine(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.description)
    counter = 0
    flag = True
    number_of_rounds = 3
    while counter < number_of_rounds:
        question, perfect_answer = game.logic()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer == perfect_answer:
            print("Correct!")
            counter += 1
        else:
            flag = False
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{perfect_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    if flag:
        print(f"Congratulations, {name}!")
