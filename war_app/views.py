from django.shortcuts import render
import war

# Create your views here.

def home_action(request):
    return render(request, 'home.html')

def game_action(request):
    context = {}
    context['game_info'] = war.play_game()
    return render(request, 'game.html', context)
