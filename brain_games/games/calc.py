import random


def description():
    calc_description = 'What is the result of the expression?'
    return calc_description


def logic():
    number_1 = random.randrange(100)
    number_2 = random.randrange(100)
    operator = random.randrange(1, 4)
    if operator == 1:
        calc_perfect_answer = number_1 + number_2
        calc_question = f'Question: {number_1} + {number_2}'
    elif operator == 2:
        calc_perfect_answer = number_1 - number_2
        calc_question = f'Question: {number_1} - {number_2}'
    else:
        calc_perfect_answer = number_1 * number_2
        calc_question = f'Question: {number_1} * {number_2}'
    return calc_question, calc_perfect_answer
