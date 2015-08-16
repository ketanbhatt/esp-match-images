from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models import F
from .models import *

import requests 


socketURL = settings.SOCKET_URL

def index(request):
	return render(request, 'esp_game/index.html')

def setup_game(request):
	old_game = Game.objects.filter(players=1).first()
	if old_game:
		print "old game"
		old_game.players = F('players') + 1
		old_game.save()
		r = requests.post(socketURL + '/pair', json={'game': old_game.id})
		return redirect('esp_game:start_game', game_id=old_game.id)
	else:
		print "new game"
		new_game = Game()
		new_game.save()
		context = {
			'game': new_game,
			'socketURL': socketURL
		}
		return render(request, 'esp_game/wait.html', context)

def start_game(request, game_id):
	print "start game"
	game = Game.objects.get(id=game_id)
	context = {
		'game': game,
		'socketURL': socketURL
	}
	return render(request, 'esp_game/start.html', context)