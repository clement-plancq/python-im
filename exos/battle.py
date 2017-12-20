import sys
import math

# soluce pour https://www.codingame.com/training/medium/winamax-battle

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

order = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')
player_1 = []
player_2 = []

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    player_1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    player_2.append(cardp_2)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

manches = 0
winners = list()
defausse_p1 = list()
defausse_p2 = list()

while len(player_1) > 0 and len(player_2) > 0:
#for i in range(min(len(player_1), len(player_2))):
    if not(len(defausse_p1) > 0):
        manches += 1
    card_p1 = player_1.pop(0)
    card_p2 = player_2.pop(0)
    print("{} - {}".format(card_p1, card_p2), file=sys.stderr)

    # bataille
    if card_p1[:-1] == card_p2[:-1]:
        print("bataille", file=sys.stderr)
        defausse_p1.append(card_p1)
        defausse_p2.append(card_p2)
        for i in range(3):
            try:
                defausse_p1.append(player_1.pop(0))
                defausse_p2.append(player_2.pop(0))
            except IndexError:
                print("PAT")
                sys.exit()
    # p1 gagne
    elif order.index(card_p1[:-1]) < order.index(card_p2[:-1]):
        if len(defausse_p1) > 0:
            player_1.extend(defausse_p1)
            player_1.append(card_p1)
            defausse_p1 = list()
            player_1.extend(defausse_p2)
            player_1.append(card_p2)
            defausse_p2 = list()
        else:
            player_1.append(card_p1)
            player_1.append(card_p2)
        winners.append(1)
        print("player 1 gagne", file=sys.stderr)
        if len(player_2) == 0:
            print("{} {}".format(1, manches))
            sys.exit()

    # p2 gagne
    else:
        if len(defausse_p1) > 0:
            player_2.extend(defausse_p1)
            player_2.append(card_p1)
            defausse_p1 = list()
            player_2.extend(defausse_p2)
            player_2.append(card_p2)
            defausse_p2 = list()
        else:
            player_2.append(card_p1)
            player_2.append(card_p2)
        winners.append(2)
        print("player 2 gagne", file=sys.stderr)
        if len(player_1) == 0:
            print("{} {}".format(2, manches))
            sys.exit()

print("PAT")
