from random import randint, randrange

description = 'What number is missing in the progression?'


def make_progression():
    """
    Return a progression of random length
    with a random first element and a random step.
    """
    length = randint(5, 10)
    first_element = randint(1, 20)
    step = randint(2, 7)
    progression = []
    for i in range(length):
        progression.append(first_element + i * step)
    return progression


def make_question(progression, index_question):
    """
    Construct and return a question
    based on the progression and index of the missing element.

    Args:
        progression: list
        index_question: int
    """
    progression_for_question = progression.copy()
    progression_for_question.pop(index_question)
    progression_for_question.insert(index_question, '..')
    question = ' '.join([str(x) for x in progression_for_question])
    return question


def logic():
    """
    Create a progression, select a random element, create and return a question
    and the expected answer.
    """
    progression = make_progression()
    index_question = randrange(len(progression))
    question = make_question(progression, index_question)
    pr_perfect_answer = str(progression[index_question])
    return question, pr_perfect_answer
