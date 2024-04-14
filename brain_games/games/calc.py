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
    return question, str(calc_perfect_answer)
