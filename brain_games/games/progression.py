import random


description = 'What number is missing in the progression?'


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
    question = ' '.join([str(x) for x in result])
    return question, str(pr_perfect_answer)
