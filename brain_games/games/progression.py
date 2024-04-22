from random import randint, randrange

DESCRIPTION = 'What number is missing in the progression?'
NIN_LENGTH = 5
MAX_LENGTH = 10
MIN_INITIAL = 1
MAX_INITIAL = 20
MIN_DIFFERENCE = 2
MAX_DIFFERENCE = 7


def make_progression(length, initial, difference):
    """
    Return a progression with the given parameters.

    Args:
    length: int
    initial: int
    difference: int
    """
    progression = []
    for i in range(length):
        progression.append(initial + i * difference)
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
    length_of_progression = randint(NIN_LENGTH, MAX_LENGTH)
    initial_of_progression = randint(MIN_INITIAL, MAX_INITIAL)
    difference_of_progression = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    progression = make_progression(length_of_progression,
                                   initial_of_progression,
                                   difference_of_progression
                                   )
    index_question = randrange(len(progression))
    question = construct_question(progression, index_question)
    perfect_answer = str(progression[index_question])
    return question, perfect_answer
