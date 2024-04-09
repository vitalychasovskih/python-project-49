import random


def description():
    prime_description = ('Answer "yes" if given number is prime. '
                         'Otherwise answer "no".')
    return prime_description


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def logic():
    number = random.randrange(100)
    if is_prime(number):
        prime_perfect_answer = 'yes'
    else:
        prime_perfect_answer = 'no'
    prime_question = f'Question: {number}'
    return prime_question, prime_perfect_answer
