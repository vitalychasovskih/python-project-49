from random import randrange
from math import gcd

description = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def make_question_and_perfect_answer():
    """
    Create two random numbers, create and return a question and the expected
    answer.
    """
    number_1 = randrange(MAX_NUMBER)
    number_2 = randrange(MAX_NUMBER)
    question = f'{number_1} {number_2}'
    perfect_answer = gcd(number_1, number_2)
    return question, str(perfect_answer)
