from random import randrange

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def logic():
    """
    Create a number, create and return a question and the expected answer.
    """
    number = randrange(100)
    even_perfect_answer = 'yes' if number % 2 == 0 else 'no'
    question = f'{number}'
    return question, even_perfect_answer
