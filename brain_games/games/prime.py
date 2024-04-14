from random import randrange

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def logic():
    number = randrange(100)
    if is_prime(number):
        prime_perfect_answer = 'yes'
    else:
        prime_perfect_answer = 'no'
    question = f'{number}'
    return question, prime_perfect_answer
