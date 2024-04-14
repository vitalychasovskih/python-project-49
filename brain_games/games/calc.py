from random import randrange, choice

description = 'What is the result of the expression?'


def logic():
    """
    Create two random numbers, chose a random operator,
    create and return a question and the expected answer.
    """
    number_1 = randrange(100)
    number_2 = randrange(100)
    operator = choice(['+', '-', '*'])
    question = f'{number_1} {operator} {number_2}'
    calc_perfect_answer = eval(question)
    # operator = randrange(1, 4)
    # if operator == 1:
    #     calc_perfect_answer = number_1 + number_2
    #     question = f'{number_1} + {number_2}'
    # elif operator == 2:
    #     calc_perfect_answer = number_1 - number_2
    #     question = f'{number_1} - {number_2}'
    # else:
    #     calc_perfect_answer = number_1 * number_2
    #     question = f'{number_1} * {number_2}'
    return question, str(calc_perfect_answer)
