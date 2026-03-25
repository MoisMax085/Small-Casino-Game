from roulette import bigger_or_smaller
from blackjack import blackjack
from colorama import init, Fore, Back
import os
from modules import wrong_answer


init(autoreset=True)
list_of_games = {"1": "Блэкджек", "2": "Рулетка", "3": "Закончить игру"}

def ask_game():
    print(
        f"{'=' * 100}\n"
        "В какую игру вы хотите сыграть ?\n"
        f"{Fore.RED}1{Fore.RESET}. Блэкджек\n"
        f"{Fore.RED}2{Fore.RESET}. Рулетка\n"
        f"{Fore.RED}3{Fore.RESET}. Закончить игру\n"
        f"{'=' * 100}"
    )
    name = input()
    if name not in list_of_games.keys() and name not in list_of_games.values():
        wrong_answer()
        ask_game()
    return name

def ask_money():
    try:
        money = int(input("\nВведите количество фишек для начала игры: "))
        return money
    except ValueError:
        wrong_answer()
        ask_money()

def start_game(name, count):
    if name == "1" or name == "Блэкджек":
        blackjack(count)
    if name == "2" or name == "Рулетка":
        bigger_or_smaller(count)
    if name == "3" or name == "Закончить игру":
        print("\nИгра завершена !")
        return
    return

def check_money():
    if os.path.exists('money.txt'):
        with open('money.txt', 'r', encoding='utf-8') as f:
            count = int(f.readline())
            if count == 0:
                print("Так уж и быть, дадим вам " + f"{Fore.RED}1000{Fore.RESET} фишек")
                count = 1000
    else:
        with open('money.txt', 'w', encoding='utf-8') as f:
            count = ask_money()
            f.write(str(count))
    return count

if __name__ == '__main__':
    amount = check_money()
    name = ask_game()
    while name != "3":
        os.system("cls" if os.name == "nt" else "clear")
        start_game(name, amount)
        name = ask_game()
