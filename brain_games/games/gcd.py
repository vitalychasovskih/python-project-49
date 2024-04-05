from brain_games.cli import welcom_user
from brain_games.engine import show_description, show_question
from brain_games.engine import cheking_the_answer
from brain_games.engine import br_gcd
from brain_games.constants import NUMBER_OF_ROUNDS


print('Welcome to the Brain Games!')
name = welcom_user()


def gcd():
    description, question, perfect_answer = br_gcd()
    show_description(description)
    counter = 0
    while counter < NUMBER_OF_ROUNDS:
        description, question, perfect_answer = br_gcd()
        show_question(question)
        answer = int(input('Your answer: '))
        chek = cheking_the_answer(answer, perfect_answer)
        if chek:
            print("Correct!")
            counter += 1
        else:
            lost_message = (
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{perfect_answer}'."
            )
            print(lost_message)
            print(f"Let's try again, {name}!")
            break
    print(f"Congratulations, {name}!")