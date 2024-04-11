import random


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def logic():
    number = random.randrange(100)
    even_perfect_answer = 'yes' if number % 2 == 0 else 'no'
    even_question = f'Question: {number}'
    return even_question, even_perfect_answer
