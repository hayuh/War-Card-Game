from django.shortcuts import render
import war
from war_app.models import *

# Renders home page.
def home_action(request):
    return render(request, 'home.html')

#Starts game when page is visited.
def game_action(request):
    #If players do not exist in database, add them
    if(len(Player.objects.filter(username="player_1")) == 0):
        player_1 = Player(username="player_1", games_won=0)
        player_1.save()
    if(len(Player.objects.filter(username="player_2")) == 0):
        player_2 = Player(username="player_2", games_won=0)
        player_2.save()
    assert len(Player.objects.filter(username="player_1")) == 1 and len(Player.objects.filter(username="player_2")) == 1
    player_1 = Player.objects.filter(username="player_1")[0]
    player_2 = Player.objects.filter(username="player_2")[0]
    context = {}
    player_1_deck, player_2_deck = war.deal_cards()
    num_war_deals = 2
    #Retrieve game information such as players' scores in each round and store them in a context dictionary to be passed
    #into rendering of HTML page.
    context['game_info'] = war.play_game(player_1_deck, player_2_deck, num_war_deals)
    #Increase players' lifetime wins and save in database.
    if(context['game_info']['winner'] == "Player 1"):
        player_1.games_won += 1
        player_1.save()
    elif(context['game_info']['winner'] == "Player 2"):
        player_2.games_won += 1
        player_2.save()
    return render(request, 'game.html', context)

#Render page to display lifetime wins.
def lifetime_wins_action(request):
    context = {"num_players": 0}
    players = Player.objects.all()
    if(len(players) != 0):
        for player in players:
            context["num_players"] += 1
            context.update({player.username: player.games_won})
    return render(request, 'lifetime_wins.html', context)

#Delete lifetime wins information.
def delete_wins_action(request):
    context = {"num_players": 0}
    print('TESt')
    Player.objects.all().delete()
    return render(request, 'lifetime_wins.html', context)
