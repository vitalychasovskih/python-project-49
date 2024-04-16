from random import randrange, choice

description = 'What is the result of the expression?'


def make_question_and_answer():
    """
    Create two random numbers, chose a random operator,
    create and return a quest
    ion and the expected answer.
    """
    number_1 = randrange(50)
    number_2 = randrange(10)
    if number_1 < number_2:
        number_1, number_2 = number_2, number_1
    operator = choice(['+', '-', '*'])
    question = f'{number_1} {operator} {number_2}'
    calc_perfect_answer = eval(question)
    return question, str(calc_perfect_answer)
