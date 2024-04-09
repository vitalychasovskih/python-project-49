from brain_games.cli import welcom_user
from brain_games.constants import NUMBER_OF_ROUNDS


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


def checking_the_answer(answer, perfect_answer):
    # нужно получить ответ пользователя и сравнить его с эталонным ответом
    # если ответ неправильный - вернуть False
    # если ответ верный - вернуть True
    return answer == perfect_answer


def round_result():
    # нужно получить из функции checking_the_answer() булево значение
    # если False - вывести сообщение о проигрыше
    # если True - увеличить счетчик на единицу
    # если счетчик набрал необходимое значение - вывести поздравление
    pass


def brain_engine(game):
    print('Welcome to the Brain Games!')
    name = welcom_user()
    show_description(game.description())
    counter = 0
    flag = True
    while counter < NUMBER_OF_ROUNDS:
        question, perfect_answer = game.logic()
        show_question(question)
        answer = input('Your answer: ')
        check = checking_the_answer(answer, perfect_answer)
        if check:
            print("Correct!")
            counter += 1
        else:
            flag = False
            lost_message = (
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{perfect_answer}'."
            )
            print(lost_message)
            print(f"Let's try again, {name}!")
            break
    if flag:
        print(f"Congratulations, {name}!")
