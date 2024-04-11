import random


description = 'What number is missing in the progression?'
# Логику игрового модуля progression можно условно поделить на 3 этапа:
# 1) вычисление членов прогрессии,
# 2) построение строки вопроса
#     (преобразование прогрессии в строку и скрытие элемента),
# 3) вычисление правильного ответа.
# Первые два лучше выделить в отдельные функции.


def make_progression():
    length = random.randint(5, 10)
    first_element = random.randint(1, 20)
    step = random.randint(2, 7)
    progression = []
    for i in range(length):
        progression.append(first_element + i * step)
    return progression


def make_question(progression, index_question):
    progression_for_question = progression.copy()
    progression_for_question.pop(index_question)
    progression_for_question.insert(index_question, '..')
    question = ' '.join([str(x) for x in progression_for_question])
    return question


def logic():
    progression = make_progression()
    index_question = random.randrange(len(progression))
    question = make_question(progression, index_question)
    pr_perfect_answer = str(progression[index_question])
    return question, pr_perfect_answer
