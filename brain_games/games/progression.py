import random


def description():
    pr_description = 'What number is missing in the progression?'
    return pr_description


def logic():
    length = random.randint(5, 10)
    first_element = random.randint(1, 20)
    step = random.randint(2, 7)
    index_question = random.randrange(length)
    result = []
    for i in range(length):
        result.append(first_element + i * step)
    pr_perfect_answer = result.pop(index_question)
    result.insert(index_question, '..')
    pr_question = 'Question: '
    pr_question += ' '.join([str(x) for x in result])
    return pr_question, pr_perfect_answer
