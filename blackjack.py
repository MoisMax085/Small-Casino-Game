import time
import os
import random
from colorama import init, Fore, Back
from modules import ask_stavka


init(autoreset=True)


suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
hidden_card = {}

def draw_card(rank, suit):
    left = f"{rank:<2}"
    right = f"{rank:>2}"
    card = [
        "┌─────────┐",
        f"│{left}       │",
        "│         │",
        f"│    {suit}    │",
        "│         │",
        f"│       {right}│",
        "└─────────┘"
    ]
    return "\n".join(card)

def return_random_card():
    rank, suit = random.randrange(0, 13), random.randrange(0, 4)
    return rank, suit

def print_cards_in_line(cards):
    for i in range(len(cards[0])):
        for card in cards:
            print(card[i], end="  ")
        print()

def show_table(crupie_cards, player_cards):
    os.system("cls" if os.name == "nt" else "clear")
    print("Карты крупье:")
    if crupie_cards:
        print_cards_in_line(crupie_cards)
    print("\nКарты игрока:")
    if player_cards:
        print_cards_in_line(player_cards)

def appending(rank, box):
    if rank >= 10:  # J, Q, K
        box.append(10)
    elif rank == 0:  # T
        box.append(11)
    else:
        box.append(int(ranks[rank]))

def hod_crupie_first(crupie_cards, amount_crupie, player_cards):
    rank, suit = return_random_card()
    appending(rank, amount_crupie)
    hidden_card.clear()
    hidden_card['rank'] = rank
    hidden_card['suit'] = suit
    crupie_cards.append(draw_card("*", "*").splitlines())
    show_table(crupie_cards, player_cards)
    time.sleep(1.3)

def hod_crupie(crupie_cards, amount_crupie, player_cards):
    rank, suit = return_random_card()
    appending(rank, amount_crupie)
    crupie_cards.append(draw_card(ranks[rank], suits[suit]).splitlines())
    show_table(crupie_cards, player_cards)
    time.sleep(1.3)

def hod_player(crupie_cards, amount_player, player_cards):
    rank, suit = return_random_card()
    appending(rank, amount_player)
    player_cards.append(draw_card(ranks[rank], suits[suit]).splitlines())
    show_table(crupie_cards, player_cards)
    time.sleep(1.3)

def ask_player(cas):
    if cas == 1:
        return int(input(f"\n{Fore.CYAN}1{Fore.RESET}. Оставить карты\n{Fore.CYAN}2{Fore.RESET}. Взять карту\nВаш выбор: "))

def open_crupies_cards(amount_crupie, crupie_cards, player_cards, hidden_card):
    crupie_cards.pop(0)
    rank = hidden_card['rank']
    suit = hidden_card['suit']
    crupie_cards.insert(0, draw_card(ranks[rank], suits[suit]).splitlines())
    show_table(crupie_cards, player_cards)

def rules(res, amount_crupie, amount_player, cas, crupie_cards, player_cards, stavka, amount):
    if cas == 0:
        open_crupies_cards(amount_crupie, crupie_cards, player_cards, hidden_card)
        if sum(amount_crupie) == 21 and sum(amount_player) == 21:
            result_of_game(4, amount, stavka)
            return
        elif sum(amount_crupie) == 21:
            result_of_game(1, amount, stavka)
            return
        elif sum(amount_player) == 21:
            result_of_game(3, amount, stavka)
            return

    if cas == 1:
        if res == 2:
            hod_player(crupie_cards, amount_player, player_cards)
            if sum(amount_player) > 21:
                open_crupies_cards(amount_crupie, crupie_cards, player_cards, hidden_card)
                result_of_game(1, amount, stavka)
                return
            elif sum(amount_player) == 21:
                res = 1
            else:
                res2 = ask_player(cas)
                rules(res2, amount_crupie, amount_player, cas, crupie_cards, player_cards, stavka, amount)
                return

        if res == 1:
            open_crupies_cards(amount_crupie, crupie_cards, player_cards, hidden_card)

            while sum(amount_crupie) <= 16:
                hod_crupie(crupie_cards, amount_crupie, player_cards)

            player_sum = sum(amount_player)
            crupie_sum = sum(amount_crupie)

            if crupie_sum > 21:
                result_of_game(2, amount, stavka)
            elif player_sum > 21:
                result_of_game(1, amount, stavka)
            elif crupie_sum > player_sum:
                result_of_game(1, amount, stavka)
            elif crupie_sum < player_sum:
                result_of_game(2, amount, stavka)
            else:
                result_of_game(4, amount, stavka)

def result_of_game(pos, amount, stavka):
    if pos == 1:
        amount -= stavka
        print("="*100 + f"\n{Fore.RED}Вы проиграли !{Fore.RESET}\nУ вас осталось {Fore.RED}{amount}{Fore.RESET} фишек. \n"+ "="*100)
    elif pos == 2:
        amount += stavka
        print("="*100 + f"\n{Fore.GREEN}Вы выиграли !{Fore.RESET}\nТеперь у вас {Fore.GREEN}{amount}{Fore.RESET} фишек.\n"+ "="*100)
    elif pos == 3:
        amount += stavka * 1.5
        print("="*100 + f"\n {Fore.MAGENTA}Блэкджэк ! Вы выиграли !{Fore.RESET}\nТеперь у вас {Fore.RED}{amount}{Fore.RESET} фишек.\n"+ "="*100)
    elif pos == 4:
        print("="*100 + f"\n Ничья !У вас {Fore.RED}{amount}{Fore.RESET} фишек.\n"+ "="*100)

    time.sleep(2.5)
    os.system("cls" if os.name == "nt" else "clear")
    f = open('money.txt', 'w')
    f.write(f'{amount}')
    f.close()





def blackjack(amount):

    stavka = ask_stavka()

    print("Запуск блэкджека")
    time.sleep(1)

    amount_crupie = []
    amount_player = []
    crupie_cards = []
    player_cards = []

    hod_player(crupie_cards, amount_player, player_cards)
    hod_crupie_first(crupie_cards, amount_crupie, player_cards)
    hod_player(crupie_cards, amount_player, player_cards)
    hod_crupie(crupie_cards, amount_crupie, player_cards)

    cas = 0
    res = 0
    rules(res, amount_crupie, amount_player, cas, crupie_cards, player_cards, stavka, amount)

    cas = 1
    res = ask_player(cas)
    rules(res, amount_crupie, amount_player, cas, crupie_cards, player_cards, stavka, amount)

