from django.shortcuts import render
import war
from war_app.models import *

# Create your views here.

def home_action(request):
    return render(request, 'home.html')

def game_action(request):
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
    context['game_info'] = war.play_game()
    if(context['game_info']['winner'] == "Player 1"):
        player_1.games_won += 1
        player_1.save()
    elif(context['game_info']['winner'] == "Player 2"):
        player_2.games_won += 1
        player_2.save()
    return render(request, 'game.html', context)
