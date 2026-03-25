from modules import *
import time
import random
import sys
import os


def check_number(answer, number_player):
    if answer == 1 and -1 < number_player < 11:
        return True
    elif answer == 2 and -1 < number_player < 21:
        return True
    elif answer == 3 and -1 < number_player < 101:
        return True
    else:
        wrong_answer()

def ask_number_player(answer, stavka, amount):
    number_player = int(input("\nВведите число : "))
    os.system("cls" if os.name == "nt" else "clear")
    if check_number(answer, number_player) == True:
        print("\nКрутим рулетку\n")
        num = spin(answer)
        time.sleep(1.3)
        rules(amount, number_player, num, stavka, answer)
    return


def spin(answer):
    k = 0
    match answer:
        case 1: k = 11
        case 2: k = 21
        case 3: k = 101
    items = [str(i) for i in range(k)]
    window_size = 5
    spins = 30
    delay = 0.05

    COLOR_RESET = "\033[0m"
    COLOR_HIGHLIGHT = "\033[0;36m"

    roulette = [random.choice(items) for _ in range(window_size)]

    for i in range(spins):
        new_item = random.choice(items)
        roulette.append(new_item)

        visible_window = roulette[-window_size:]
        middle_index = window_size // 2
        display_window = ""
        for idx, val in enumerate(visible_window):
            if idx == middle_index:
                display_window += COLOR_HIGHLIGHT + val + COLOR_RESET + " "
            else:
                display_window += val + " "

        sys.stdout.write("\r" + display_window.strip())
        sys.stdout.flush()

        time.sleep(delay)
        delay *= 1.05

    final_value = roulette[-window_size + middle_index]
    print(f"\n\nРулетка остановилась! Выпало: {final_value}\n")
    return int(final_value)


def rules(amount, number_player, num, stavka, answer):
    if num == number_player:
        mnozh = 0
        match answer:
            case 1:
                mnozh = 10
            case 2:
                mnozh = 20
            case 3:
                mnozh = 100
        amount += stavka * mnozh
        print("="*100 + f"\n{Fore.GREEN}Вы выиграли !{Fore.RESET}\nТеперь у вас {Fore.GREEN}{amount}{Fore.RESET} фишек.\n"+ "="*100)
    else:
        amount -= stavka
        print("="*100 + f"\n{Fore.RED}Вы проиграли !{Fore.RESET}\nУ вас осталось {Fore.RED}{amount}{Fore.RESET} фишек. \n"+ "="*100)
    time.sleep(2.5)
    os.system("cls" if os.name == "nt" else "clear")
    f = open('money.txt', 'w')
    f.write(f'{amount}')
    f.close()


def ask_amount_of_numbers():
    os.system("cls" if os.name == "nt" else "clear")
    answer = int(input("="*100 + "\nВыберите в каком диапазоне вы хотите сыграть ?\n1. 0-10\n2. 0-20\n3. 0-100\n"+ "="*100 + "\n"))
    os.system("cls" if os.name == "nt" else "clear")
    if answer != any([1,2,3]):
        wrong_answer()
    else:
        return answer


def bigger_or_smaller(amount):
    stavka = ask_stavka()

    print("\nЗапуск игры 'Больше-меньше' ")
    time.sleep(1.2)

    answer = ask_amount_of_numbers()
    ask_number_player(answer, stavka, amount)