import random
from brain_games.cli import welcom_user


print('Welcome to the Brain Games!')
name = welcom_user()


def calc():
    number_1 = random.randrange(100)
    number_2 = random.randrange(100)
    operator = random.randrange(1, 3)
    if operator == 1:
        perfect_answer = number_1 + number_2
        question = f'Question: {number_1} + {number_2}'
    elif operator == 2:
        perfect_answer = number_1 - number_2
        question = f'Question: {number_1} - {number_2}'
    else:
        perfect_answer = number_1 * number_2
        question = f'Question: {number_1} * {number_2}'
    return question, perfect_answer


def brain_calc():
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        question, perfect_answer = calc()
        print(question)
        answer = int(input('Your answer: '))
        if answer != perfect_answer:
            lost_message = f"'{answer}' is wrong answer ;(. "
            lost_message += f"Correct answer was '{perfect_answer}'."
            print(lost_message)
            print("Let's try again!")
            break
        else:
            print("Correct!")
            counter += 1
            if counter == 3:
                print(f"Congratulations, {name}!")
