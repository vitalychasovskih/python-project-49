from random import randint, randrange

description = 'What number is missing in the progression?'


def make_progression(length, first_element, step):
    """
    Return a progression with the given parameters.

    Args:
    length: int
    first_element: int
    step: int
    """
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
    length = randint(5, 10)
    first_element = randint(1, 20)
    step = randint(2, 7)
    progression = make_progression(length, first_element, step)
    index_question = randrange(len(progression))
    question = make_question(progression, index_question)
    pr_perfect_answer = str(progression[index_question])
    return question, pr_perfect_answer
