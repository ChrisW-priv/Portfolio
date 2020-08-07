number = 1

player = ""
player_1 = ""
player_2 = ""
player_3 = ""
player_4 = ""

dropped_out = False
dropped_out_1 = False
dropped_out_2 = False
dropped_out_3 = False
dropped_out_4 = False

print(" Please state if you want to play with or friends (number of players) (c)comp.")
game = input(" > ")


def win():
    pass


def answer(num):
    if not num % 3 and not num % 5:
        return "Fizz Buzz"
    elif not num % 3:
        return "Fizz"
    elif not num % 5:
        return "Buzz"
    else:
        return str(num)


def multi_player_game():

    global dropped_out_1, dropped_out_2, dropped_out_3, dropped_out_4,\
        player_1, player_2, player_3, player_4, number
    if not dropped_out_1:
        player_1 = input(" > What is next? (1) ")
        if player_1 == "k":
            dropped_out_1 = True
        elif player_1.lower() != answer(number).lower():
            print("Sorry you lost")
            dropped_out_1 = True
        else:
            print("that is correct")
            number += 1
    if not dropped_out_2:
        player_2 = input(" > What is next? (2) ")
        if player_2 == "k":
            dropped_out_2 = True
        elif player_2.lower() != answer(number).lower():
            print("Sorry you lost")
            dropped_out_2 = True
        else:
            print("that is correct")
            number += 1
    if not dropped_out_3 and int(game) >= 3:
        player_3 = input(" > What is next? (3) ")
        if player_3 == "k":
            dropped_out_3 = True
        elif player_3.lower() != answer(number).lower():
            print("Sorry you lost")
            dropped_out_3 = True
        else:
            print("That is correct")
            number += 1
    if not dropped_out_4 and int(game) == 4:
        player_4 = input(" > What is next? (4) ")
        if player_4 == "k":
            dropped_out_4 = True
        elif player_4.lower() != answer(number).lower():
            print("Sorry you lost")
            dropped_out_4 = True
        else:
            print("that is correct")
            number += 1


def comp_game():
    global number, player, dropped_out
    if not dropped_out:
        print(answer(number))
        number += 1
        player = input(" > What should be next? ")
        if player == "k":
            print("you have quited the game")
            dropped_out = True
        elif not player.lower() == answer(number).lower():
            print("Sorry you lost")
            dropped_out = True
        number += 1


if game == "c" or game == 1:
    print("Computer will start...\n")

while True:
    if game == "c" or game == "1":
        comp_game()
    elif game == "2" or game == "3" or game == "4":
        multi_player_game()
    else:
        print("You did not insert correct value, please type in number of players or 'c' to play with computer")
