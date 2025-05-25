"""
main.py: druhý projekt do Engeto Online Python Akademie

author:  Marek Sedlák
email:   sedlak.marek14@icloud.com
"""

import random
import time

def pozdrav():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------")

def generuj_tajne_cislo():
    # první číslice 1-9 (nesmí být 0), další 3 libovolné 0-9 bez duplicit
    while True:
        cislo = random.sample('123456789', 1) + random.sample('0123456789', 3)
        cislo_str = ''.join(cislo)
        if len(set(cislo_str)) == 4:
            return cislo_str

def je_validni_tip(tip):
    if len(tip) != 4:
        print("Error: Number must have exactly 4 digits.")
        return False
    if not tip.isdigit():
        print("Error: Input must contain only digits.")
        return False
    if tip[0] == '0':
        print("Error: Number cannot start with zero.")
        return False
    if len(set(tip)) != 4:
        print("Error: Digits must be unique.")
        return False
    return True

def vyhodnot_tip(tip, tajne_cislo):
    bulls = sum(tip[i] == tajne_cislo[i] for i in range(4))
    cows = sum((c in tajne_cislo) for c in tip) - bulls
    return bulls, cows

def formatuj_bulls_cows(bulls, cows):
    bulls_text = f"{bulls} bull" + ("s" if bulls != 1 else "")
    cows_text = f"{cows} cow" + ("s" if cows != 1 else "")
    return bulls_text, cows_text

def hra():
    pozdrav()
    tajne_cislo = generuj_tajne_cislo()
    # print(f"DEBUG tajne číslo: {tajne_cislo}")  # pro ladění

    pocet_pokusu = 0
    start = time.time()

    while True:
        tip = input(">>> ").strip()
        if not je_validni_tip(tip):
            continue

        pocet_pokusu += 1
        bulls, cows = vyhodnot_tip(tip, tajne_cislo)

        if bulls == 4:
            konec = time.time()
            cas = konec - start
            print("Correct, you've guessed the right number")
            print(f"in {pocet_pokusu} guess{'es' if pocet_pokusu != 1 else ''}!")
            print("-----------------------------------------------")
            print("That's amazing!")
            print(f"Time taken: {cas:.2f} seconds.")
            print("-----------------------------------------------")
            return pocet_pokusu, cas

        bulls_text, cows_text = formatuj_bulls_cows(bulls, cows)
        print(f"{bulls_text}, {cows_text}")
        print("-----------------------------------------------")

def hlavni():
    statistiky = []
    while True:
        pokusy, cas = hra()
        statistiky.append(pokusy)
        prumer = sum(statistiky) / len(statistiky)
        print(f"Average number of guesses: {prumer:.2f}")

        znovu = input("Play again? (y/n): ").strip().lower()
        if znovu != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    hlavni()
