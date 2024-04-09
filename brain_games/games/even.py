import random


def description():
    even_description = 'Answer "yes" if the number is even, '
    even_description += 'otherwise answer "no".'
    return even_description


def logic():
    number = random.randrange(100)
    even_perfect_answer = 'yes' if number % 2 == 0 else 'no'
    even_question = f'Question: {number}'
    return even_question, even_perfect_answer
