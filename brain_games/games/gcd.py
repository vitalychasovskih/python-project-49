from random import randrange
from math import gcd

description = 'Find the greatest common divisor of given numbers.'


def logic():
    number_1 = randrange(100)
    number_2 = randrange(100)
    question = f'{number_1} {number_2}'
    gcd_perfect_answer = gcd(number_1, number_2)
    return question, str(gcd_perfect_answer)
