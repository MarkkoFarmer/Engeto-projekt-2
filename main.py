"""
main.py: druhý projekt do Engeto Online Python Akademie

author:  Marek Sedlák
email:   sedlak.marek14@icloud.com
"""

import random
import time

def vypis_hranic():
    print("-----------------------------------------------")

def pozdrav():
    print("Hi there!")
    vypis_hranic()
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    vypis_hranic()
    print("Enter a number:")
    vypis_hranic()

def generuj_tajne_cislo():
    prvni = random.choice("123456789")
    zbytek = random.sample([c for c in "0123456789" if c != prvni], 3)
    return prvcni + ''.join(zbytek)

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
    bulls = sum(a == b for a, b in zip(tip, tajne_cislo))
    cows = sum(min(tip.count(d), tajne_cislo.count(d)) for d in set(tip)) - bulls
    return bulls, cows

def formatuj_bulls_cows(bulls, cows):
    bulls_text = f"{bulls} bull" + ("s" if bulls != 1 else "")
    cows_text = f"{cows} cow" + ("s" if cows != 1 else "")
    return bulls_text, cows_text

def hra():
    pozdrav()
    tajne_cislo = generuj_tajne_cislo()
    # print(f"DEBUG: Tajné číslo je {tajne_cislo}")  # Pro ladění

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
            vypis_hranic()
            print("That's amazing!")
            print(f"Time taken: {cas:.2f} seconds.")
            vypis_hranic()
            return pocet_pokusu, cas

        bulls_text, cows_text = formatuj_bulls_cows(bulls, cows)
        print(f"{bulls_text}, {cows_text}")
        vypis_hranic()

def hlavni():
    statistiky = []
    while True:
        pokusy, cas = hra()
        statistiky.append({"pokusy": pokusy, "cas": cas})

        prumer_pokusu = sum(stat["pokusy"] for stat in statistiky) / len(statistiky)
        prumer_casu = sum(stat["cas"] for stat in statistiky) / len(statistiky)
        print(f"Average number of guesses: {prumer_pokusu:.2f}")
        print(f"Average time: {prumer_casu:.2f} seconds")

        znovu = input("Play again? (y/n): ").strip().lower()
        if znovu != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    hlavni()
