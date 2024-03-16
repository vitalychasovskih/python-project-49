import random
from .cli import welcom_user


print('Welcome to the Brain Games!')
name = welcom_user()


def is_number_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randrange(100)
        if number % 2 == 0:
            perfect_answer = 'yes'
        else:
            perfect_answer = 'no'

        print(f'Question: {number}')
        answer = input('Your answer: ')
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
