from random import randrange

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100


def is_prime(n):
    """
    Return True if n is prime and False otherwise.

    Args:
        n: int
    """
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def make_question_and_perfect_answer():
    """
    Create a number, create and return a question and the expected answer.
    """
    number = randrange(MAX_NUMBER)
    if is_prime(number):
        perfect_answer = 'yes'
    else:
        perfect_answer = 'no'
    question = f'{number}'
    return question, perfect_answer
