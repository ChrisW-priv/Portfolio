import random
import time as t

colour = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
num_of_decks = 3
pack = 4*colour*num_of_decks


def sh_deck():
    for i in range(30):
        random.shuffle(pack)
    print(pack)


def next_card():
    new_c = pack.pop(0)
    pack.append(new_c)
    return new_c


def win():
    if not player > 21 and dealer > 21:
        return True
    elif 21-player < 21-dealer and not player > 21:
        return True
    elif player > 21:
        return False
    elif 21-dealer < 21-player and not dealer > 21:
        return False


dealer = 0
player = 0


def decision():
    # player can:
    # stay
    # hit
    # double down
    # split
    intake = input(" > ")
    if intake == "hit":
        pass
    elif intake == "stay":
        pass
    elif intake == "dd":
        pass
    elif intake == "split":
        pass
    else:
        pass


def game():
    global dealer, player
    player += next_card()
    dealer += next_card()
    player += next_card()
    dealer += next_card()
    print(f"Dealers hand is: {dealer}\nYour hand is: {player}")
    t.sleep(7)
    # decision of player
    while True:
        if dealer <= 16:
            dealer += next_card()
        else:
            break


sh_deck()
game()
print(f"\n True if u win, False if not: {win()}\n")

print(dealer)
print(player)
