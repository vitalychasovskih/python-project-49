from random import randint, randrange

description = 'What number is missing in the progression?'
NIN_LENGTH = 5
MAX_LENGTH = 10
MIN_FIRST = 1
MAX_FIRST = 20
MIN_STEP = 2
MAX_STEP = 7


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


def construct_question(progression, index_question):
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


def make_question_and_perfect_answer():
    """
    Create a progression, select a random element, create and return a question
    and the expected answer.
    """
    length_progression = randint(NIN_LENGTH, MAX_LENGTH)
    first_element_progression = randint(MIN_FIRST, MAX_FIRST)
    step_progression = randint(MIN_STEP, MAX_STEP)
    progression = make_progression(length_progression,
                                   first_element_progression,
                                   step_progression
                                   )
    index_question = randrange(len(progression))
    question = construct_question(progression, index_question)
    perfect_answer = str(progression[index_question])
    return question, perfect_answer
