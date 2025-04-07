"""
Этот модуль содержит в себе движок игры, который отвечает за общую логику игр
"""

def run_game(game_logic, game_description):
    """
    Эта функция отвечает за запуск выбраной игры, а так же содержит в себе общую логику игр
    """
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")
    print(game_description)

    rounds = 3
    for _ in range(rounds):
        question, correct_answer = game_logic()
        print(f"\nQuestion: {question}")
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"\nCongratulations, {name}!")
