import random
# import time as t

colour = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
num_of_decks = 3
pack = 4*colour*num_of_decks


def sh_deck():
    for i in range(2):
        random.shuffle(pack)


def next_card():
    new_c = pack.pop(0)
    pack.append(new_c)
    return new_c


def win():
    if not sum(player) > 21 and sum(dealer) > 21:
        return "player"
    elif 21-sum(player) < 21-sum(dealer) and not sum(player) > 21:
        return "player"
    elif sum(player) > 21:
        return "dealer"
    elif 21-sum(dealer) < 21-sum(player) and not sum(dealer) > 21:
        return "dealer"
    elif sum(player) == sum(dealer):
        return "draw"


def who():
    if win() == "player":
        return "player's win"
    elif win() == "dealer":
        return "dealer's win"
    elif win() == "draw":
        return "a draw"


def decision():
    #   player can:
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


pl = 0
dl = 0
draw = 0


def outcome():
    global pl, dl, draw
    if win() == "player":
        pl += 1
    elif win() == "dealer":
        dl += 1
    elif win() == "draw":
        draw += 1
    return f"\nCurrently it is:\nPlayer: {pl}\nDealer: {dl}\nNum of draws: {draw}\n"


player = []
dealer = []
tm = 1
# actual game
while tm < 1000:
    player = []
    dealer = []
    sh_deck()
    player.append(next_card())
    dealer.append(next_card())
    player.append(next_card())
    dealer.append(next_card())
    # t.sleep(3)
    # decision of player, for now like dealer

    while sum(player) <= 16:
        if sum(player) <= 16:
            player.append(next_card())

    while sum(dealer) <= 16:
        if sum(dealer) <= 16:
            dealer.append(next_card())

    # print("Score of the player: " + str(player) + " and that is: " + str(sum(player)))
    # print("Score of the dealer: " + str(dealer) + " and that is: " + str(sum(dealer)))
    # print(f"\tSo it is {who()}")
    # print(outcome())
    outcome()
    tm += 1

print(outcome())
