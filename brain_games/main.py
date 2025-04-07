"""
Основной модуль из которого происходит запуск игры
"""

from engine import run_game
from games.lcm_game import generate_question as lcm_question, DESCRIPTION as lcm_desc
from games.progression import generate_question as prog_question, DESCRIPTION as prog_desc


def main():
    """
    Основная функция ответственная за запуск игры
    """
    games_list = {
        "lcm": (lcm_question, lcm_desc),
        "progression": (prog_question, prog_desc)
    }

    print("Select a game:")
    for key, (name, _, _) in games_list.items():
        print(f"{key}: {name}")

    choice = input("Your choice: ")

    if choice in games_list:
        _, game_logic, description = games_list[choice]
        run_game(game_logic, description)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
