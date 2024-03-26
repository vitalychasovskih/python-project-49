import random  # необходим для функций br_calc и br_even


def welcom_user():
    # уже описана в модуле brain_games.cli функция welcom_user
    pass


def show_description(description):
    # нужно получить и затем показать в зависимости от команды в терминале
    # описание для каждой конкретной игры
    # например 'What is the result of the expression?'
    print(description)


def show_question(question):
    # нужно получить и затем показать в зависимости от команды в терминале
    # вопрос после которого программа будет ожидать ответ
    # например f'Question: {number_1} * {number_2}'
    print(question)


def cheking_the_answer(answer, perfect_answer):
    # нужно получить ответ пользователя и сравнить его с эталонным ответом
    # если ответ неправильный - вернуть False
    # если ответ верный - вернуть True
    return answer == perfect_answer


def round_result():
    # нужно получить из функции cheking_the_answer() булево значение
    # если False - вывести сообщение о проигрыше
    # если True - увеличить счетчик на единицу
    # если счетчик набрал необходимое значение - вывести поздравление
    pass


def br_even():
    even_description = 'Answer "yes" if the number is even, '
    even_description += 'otherwise answer "no".'
    number = random.randrange(100)
    if number % 2 == 0:
        even_perfect_answer = 'yes'
    else:
        even_perfect_answer = 'no'
    even_question = (f'Question: {number}')
    return even_description, even_question, even_perfect_answer


def br_calc():
    calc_description = 'What is the result of the expression?'
    number_1 = random.randrange(100)
    number_2 = random.randrange(100)
    operator = random.randrange(1, 4)
    if operator == 1:
        calc_perfect_answer = number_1 + number_2
        calc_question = f'Question: {number_1} + {number_2}'
    elif operator == 2:
        calc_perfect_answer = number_1 - number_2
        calc_question = f'Question: {number_1} - {number_2}'
    else:
        calc_perfect_answer = number_1 * number_2
        calc_question = f'Question: {number_1} * {number_2}'
    return calc_description, calc_question, calc_perfect_answer


def br_gcd():
    gcd_description = 'Find the greatest common divisor of given numbers.'
    number_1 = random.randrange(100)
    number_2 = random.randrange(100)
    gcd_question = f'Question: {number_1} {number_2}'
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    gcd_perfect_answer = number_1 + number_2
    return gcd_description, gcd_question, gcd_perfect_answer


def br_progression():
    pr_description = 'What number is missing in the progression?'
    length = random.randint(5, 10)
    first_element = random.randint(1, 20)
    step = random.randint(2, 7)
    index_question = random.randrange(length)
    result = []
    for i in range(length):
        result.append(first_element + i * step)
    pr_perfect_answer = result.pop(index_question)
    result.insert(index_question, '..')
    pr_question = ('Question:', ' '.join([str(x) for x in result]))
    return pr_description, pr_question, pr_perfect_answer
