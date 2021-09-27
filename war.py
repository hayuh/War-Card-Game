import random
from collections import deque

#card deck and corresponding values
deck = {"C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7 , "C8": 8, "C9": 9, "C10": 10, "CJ": 11, "CQ": 12, "CK": 13, "CA": 14,
        "D2": 2, "D3": 3, "D4": 4, "D5": 5, "D6": 6, "D7": 7 , "D8": 8, "D9": 9, "D10": 10, "DJ": 11, "DQ": 12, "DK": 13, "DA": 14,
        "H2": 2, "H3": 3, "H4": 4, "H5": 5, "H6": 6, "H7": 7 , "H8": 8, "H9": 9, "H10": 10, "HJ": 11, "HQ": 12, "HK": 13, "HA": 14,
        "S2": 2, "S3": 3, "S4": 4, "S5": 5, "S6": 6, "S7": 7 , "S8": 8, "S9": 9, "S10": 10, "SJ": 11, "SQ": 12, "SK": 13, "SA": 14}

def deal_cards():
        cards = list(deck.keys())

        random.shuffle(cards)

        half = len(deck)//2
        player_1 = deque(cards[0:half])
        player_2 = deque(cards[half:])
        return player_1, player_2

def play_game(player_1, player_2, num_war_deals):

        game_info = {"player_1_start": list(player_1), "player_2_start": list(player_2)}
        rounds = []
        winner = ""

        while(1):
                round = dict()
                if(len(player_1) == 0):
                        winner = "Player 2"
                        break
                if(len(player_2) == 0):
                        winner = "Player 1"
                        break
                player_1_card, player_2_card = player_1.pop(), player_2.pop()
                winning_pot = [player_1_card, player_2_card]
                random.shuffle(winning_pot)
                
                if(deck[player_1_card] > deck[player_2_card]):
                        player_1.extendleft(winning_pot)
                        round = {"type": "battle", "player_1_card": player_1_card, "player_2_card": player_2_card, "winning_pot": winning_pot,
                        "player_1_deck": list(player_1), "player_2_deck": list(player_2)}
                        round.update({"player_1_num_cards": len(round["player_1_deck"]), "player_2_num_cards": len(round["player_2_deck"])})
                        rounds.append(round)
                elif(deck[player_1_card] < deck[player_2_card]):
                        player_2.extendleft(winning_pot)
                        round = {"type": "battle", "player_1_card": player_1_card, "player_2_card": player_2_card, "winning_pot": winning_pot,
                        "player_1_deck": list(player_1), "player_2_deck": list(player_2)}
                        round.update({"player_1_num_cards": len(round["player_1_deck"]), "player_2_num_cards": len(round["player_2_deck"])})
                        rounds.append(round)

                else:
                        round = {"type": "battle", "player_1_card": player_1_card, "player_2_card": player_2_card, "winning_pot": winning_pot,
                        "player_1_deck": list(player_1), "player_2_deck": list(player_2)}
                        round.update({"player_1_num_cards": len(round["player_1_deck"]), "player_2_num_cards": len(round["player_2_deck"])})
                        rounds.append(round)
                        winning_pot = [player_1_card, player_2_card]
                        war_won = False
                        while(war_won == False):
                                if(len(player_1) < num_war_deals):
                                        winner = "Player 2"
                                        break
                                if(len(player_2) < num_war_deals):
                                        winner = "Player 1"
                                        break
                                for i in range(0, num_war_deals-1):
                                        winning_pot.extend([player_1.pop(), player_2.pop()])
                                player_1_war_card, player_2_war_card = player_1.pop(), player_2.pop()
                                winning_pot.extend([player_1_war_card, player_2_war_card])
                                if(deck[player_1_war_card] > deck[player_2_war_card]):
                                        random.shuffle(winning_pot)
                                        player_1.extendleft(winning_pot)
                                        war_won = True
                                        round = {"type": "war", "player_1_card": player_1_war_card, "player_2_card": player_2_war_card, "winning_pot": winning_pot,
                                        "player_1_deck": list(player_1), "player_2_deck": list(player_2)}
                                        round.update({"player_1_num_cards": len(round["player_1_deck"]), "player_2_num_cards": len(round["player_2_deck"])})
                                        rounds.append(round)
                                elif(deck[player_1_war_card] < deck[player_2_war_card]):
                                        random.shuffle(winning_pot)
                                        player_2.extendleft(winning_pot)
                                        war_won = True
                                        round = {"type": "war", "player_1_card": player_1_war_card, "player_2_card": player_2_war_card, "winning_pot": winning_pot,
                                        "player_1_deck": list(player_1), "player_2_deck": list(player_2)}
                                        round.update({"player_1_num_cards": len(round["player_1_deck"]), "player_2_num_cards": len(round["player_2_deck"])})
                                        rounds.append(round)
                                else:
                                        round = {"type": "war", "player_1_card": player_1_war_card, "player_2_card": player_2_war_card, "winning_pot": winning_pot,
                                        "player_1_deck": list(player_1), "player_2_deck": list(player_2)}
                                        round.update({"player_1_num_cards": len(round["player_1_deck"]), "player_2_num_cards": len(round["player_2_deck"])})
                                        rounds.append(round)
                                        continue
        game_info.update({"rounds": rounds, "winner": winner})
        return game_info



def test_battle_win():
#Test if battle wins are correct. Player 2 should win.

        #make player_1 deck
        player_1 = deque(["C2"])
        player_2 = deque(["C3"])
        possible_choices = [x for x in cards if x not in list(player_1) and x not in list(player_2)]
        p1_selections = random.sample(possible_choices, 25)
        assert "C2" not in p1_selections and "C3" not in p1_selections
        assert len(set(p1_selections)) == len(p1_selections) 
        player_1.extendleft(p1_selections)

        #make player_2 deck
        p2_selections = [x for x in cards if x not in list(player_1) and x != "C3"]
        random.shuffle(p2_selections)
        assert "C2" not in p2_selections and "C3" not in p2_selections
        assert len(set(p2_selections)) == len(p2_selections) 
        player_2.extendleft(p2_selections)

        #check player_2 wins
        assert len(player_1) == len(player_2)
        game_info = play_game(player_1, player_2, 2)
        updated_player_1_deck, updated_player_2_deck = game_info["rounds"][0]["player_1_deck"], game_info["rounds"][0]["player_2_deck"]
        assert len(updated_player_2_deck) > len(updated_player_1_deck)
        assert len(updated_player_2_deck) - len(updated_player_1_deck) == 2
        assert "C2" in list(updated_player_2_deck) and "C3" in list(updated_player_2_deck)

def test_war_win_one():
#Test if war wins are correct after 1 round of war. Player 2 should win.

        #make player_1 deck
        player_1 = deque(["C2", "DA", "C3"])
        player_2 = deque(["D4", "HJ", "D3"])
        possible_choices = [x for x in cards if x not in list(player_1) and x not in list(player_2)]
        p1_selections = random.sample(possible_choices, 23)
        assert all(x not in p1_selections for x in ["C2", "C3", "D3", "D4", "DA", "HJ"])
        assert len(set(p1_selections)) == len(p1_selections) 
        player_1.extendleft(p1_selections)

        #make player_2 deck
        p2_selections = [x for x in cards if x not in list(player_1) and x not in ["C2", "C3", "D3", "D4", "DA", "HJ"]]
        random.shuffle(p2_selections)
        assert all(x not in p2_selections for x in ["C2", "C3", "D3", "D4", "DA", "HJ"])
        assert len(set(p2_selections)) == len(p2_selections) 
        player_2.extendleft(p2_selections)

        #check player_2 wins
        assert len(player_1) == len(player_2)
        game_info = play_game(player_1, player_2, 2)
        updated_player_1_deck, updated_player_2_deck = game_info["rounds"][1]["player_1_deck"], game_info["rounds"][1]["player_2_deck"]
        print(updated_player_2_deck, updated_player_1_deck)
        assert len(updated_player_2_deck) > len(updated_player_1_deck)
        assert (len(updated_player_2_deck) - len(updated_player_1_deck)) == 6
        assert all(x in list(updated_player_2_deck) for x in ["C2", "C3", "D3", "D4", "DA", "HJ"])

def test_war_win_two():
#Test if war wins are correct after 2 rounds of war. Player 2 should win.

        #make player_1 deck
        player_1 = deque(["H2", "H5", "CA", "DA", "C3"])
        player_2 = deque(["H3", "H9", "HA", "HJ", "D3"])
        possible_choices = [x for x in cards if x not in list(player_1) and x not in list(player_2)]
        p1_selections = random.sample(possible_choices, 21)
        assert all(x not in p1_selections for x in ["H2", "H5", "CA", "DA", "C3", "H3", "H9", "HA", "HJ", "D3"])
        assert len(set(p1_selections)) == len(p1_selections) 
        player_1.extendleft(p1_selections)

        #make player_2 deck
        p2_selections = [x for x in cards if x not in list(player_1) and x not in ["H2", "H5", "CA", "DA", "C3", "H3", "H9", "HA", "HJ", "D3"]]
        random.shuffle(p2_selections)
        assert all(x not in p2_selections for x in ["H2", "H5", "CA", "DA", "C3", "H3", "H9", "HA", "HJ", "D3"])
        assert len(set(p2_selections)) == len(p2_selections) 
        player_2.extendleft(p2_selections)

        #check player_2 wins
        assert len(player_1) == len(player_2)
        game_info = play_game(player_1, player_2, 2)
        updated_player_1_deck, updated_player_2_deck = game_info["rounds"][2]["player_1_deck"], game_info["rounds"][2]["player_2_deck"]
        print(updated_player_2_deck, updated_player_1_deck)
        assert len(updated_player_2_deck) > len(updated_player_1_deck)
        assert (len(updated_player_2_deck) - len(updated_player_1_deck)) == 10
        assert all(x in list(updated_player_2_deck) for x in ["H2", "H5", "CA", "DA", "C3", "H3", "H9", "HA", "HJ", "D3"])

if __name__ == "__main__":
        cards = list(deck.keys())
        test_battle_win()
        test_war_win_one()
        test_war_win_two()



