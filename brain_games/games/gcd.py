import random


description = 'Find the greatest common divisor of given numbers.'


def logic():
    number_1 = random.randrange(100)
    number_2 = random.randrange(100)
    gcd_question = f'Question: {number_1} {number_2}'
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    gcd_perfect_answer = number_1 + number_2
    return gcd_question, str(gcd_perfect_answer)
