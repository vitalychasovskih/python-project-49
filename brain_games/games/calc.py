from random import randrange

description = 'What is the result of the expression?'


def logic():
    number_1 = randrange(100)
    number_2 = randrange(100)
    operator = randrange(1, 4)
    if operator == 1:
        calc_perfect_answer = number_1 + number_2
        question = f'{number_1} + {number_2}'
    elif operator == 2:
        calc_perfect_answer = number_1 - number_2
        question = f'{number_1} - {number_2}'
    else:
        calc_perfect_answer = number_1 * number_2
        question = f'{number_1} * {number_2}'
    return question, str(calc_perfect_answer)
