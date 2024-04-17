from random import randrange, choice

DESCRIPTION = 'What is the result of the expression?'
MAX_ARGUMENT_1 = 50
MAX_ARGUMENT_2 = 10


def make_question_and_perfect_answer():
    """
    Create two random numbers, chose a random operator,
    create and return a quest
    ion and the expected answer.
    """
    number_1 = randrange(MAX_ARGUMENT_1)
    number_2 = randrange(MAX_ARGUMENT_2)
    if number_1 < number_2:
        number_1, number_2 = number_2, number_1
    operator = choice(['+', '-', '*'])
    question = f'{number_1} {operator} {number_2}'
    perfect_answer = eval(question)
    return question, str(perfect_answer)
