import random
from collections import deque

#card deck and corresponding values
deck = {"C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7 , "C8": 8, "C9": 9, "C10": 10, "CJ": 11, "CQ": 12, "CK": 13, "CA": 14,
        "D2": 2, "D3": 3, "D4": 4, "D5": 5, "D6": 6, "D7": 7 , "D8": 8, "D9": 9, "D10": 10, "DJ": 11, "DQ": 12, "DK": 13, "DA": 14,
        "H2": 2, "H3": 3, "H4": 4, "H5": 5, "H6": 6, "H7": 7 , "H8": 8, "H9": 9, "H10": 10, "HJ": 11, "HQ": 12, "HK": 13, "HA": 14,
        "S2": 2, "S3": 3, "S4": 4, "S5": 5, "S6": 6, "S7": 7 , "S8": 8, "S9": 9, "S10": 10, "SJ": 11, "SQ": 12, "SK": 13, "SA": 14}
cards = list(deck.keys())
#print(cards)
random.shuffle(cards)
print(cards)
half = len(deck)//2
print(half)
player_1 = deque(cards[0:half])
player_2 = deque(cards[half:])


print("1", player_1)
print("2", player_2)
#while(len(player1) != 0 and len(player2) != 0):
player_1_card, player_2_card = player_1.pop(), player_2.pop()
print("1", player_1)
print("2", player_2)
if(deck[player_1_card] > deck[player_2_card]):
        player_1.extendleft([player_1_card, player_2_card])
        print("1", player_1)
        print("2", player_2)
elif(deck[player_1_card] < deck[player_2_card]):
        player_2.extendleft([player_1_card, player_2_card])
        print("1", player_1)
        print("2", player_2)
else:
        winning_pot = [player_1_card, player_2_card]
        war_won = False
        while(war_won == False and (len(player_1) > 1 and len(player_2) > 1)):
                player_1_war_card_down, player_1_war_card_up = player_1.pop(), player_1.pop()
                player_2_war_card_down, player_2_war_card_up = player_2.pop(), player_2.pop()
                winning_pot.extend([player_1_war_card_down, player_1_war_card_up, player_2_war_card_down, player_2_war_card_up])
                if(deck[player_1_war_card_up] > deck[player_2_war_card_up]):
                        player_1.extendleft(winning_pot)
                        war_won = True
                        print("1", player_1)
                        print("2", player_2)
                elif(deck[player_1_war_card_up] < deck[player_2_war_card_up]):
                        player_2.extendleft(winning_pot)
                        war_won = True
                        print("1", player_1)
                        print("2", player_2)
                else:
                        continue

a = deque([1,2,3,4])
print(a)
a_down, a_up = a.pop(), a.pop()
print(a_down, a_up, a)






