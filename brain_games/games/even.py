from random import randrange

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 100


def make_question_and_perfect_answer():
    """
    Create a number, create and return a question and the expected answer.
    """
    number = randrange(MAX_NUMBER)
    perfect_answer = 'yes' if number % 2 == 0 else 'no'
    question = f'{number}'
    return question, perfect_answer
