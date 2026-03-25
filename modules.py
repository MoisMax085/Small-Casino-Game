from colorama import init, Fore, Back

def wrong_answer():
    print("\033[31m{}\033[0m".format("="*100 + "\nОшибка ввода\n" + "="*100))
    return

def ask_stavka():
    f = open('money.txt', 'r')
    amount = int(f.readline())
    count = int(input(f"\nУ вас {Fore.RED}{amount}{Fore.RESET} фишек.\nВведите вашу ставку: "))
    if count > amount:
        print(f"У вас столько нет. У вас есть {Fore.CYAN}{amount}{Fore.RESET} фишек.")
        return ask_stavka(amount)
    if count <= 0:
        print("Ставка не может быть меньше или равна нулю!")
        return ask_stavka(amount)
    return count