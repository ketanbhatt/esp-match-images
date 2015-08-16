from django.shortcuts import render, redirect
from django.http import JsonResponse
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
		requests.post(socketURL + '/pair', json={'game': old_game.id})
		randomPrimaryImage = PrimaryImage.objects.order_by('?').first()
		firstQuestion = Question(game=old_game, primaryImage=randomPrimaryImage)
		firstQuestion.save()
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
	question = Question.objects.get(game=game)
	context = {
		'game': game,
		'question': question,
		'socketURL': socketURL
	}
	return render(request, 'esp_game/start.html', context)

def ajax_submit_choice(request):
	questionId = request.POST.get('questionId')
	playerChoice = request.POST.get('playerChoice')
	curr_question = Question.objects.get(id=questionId)

	if not curr_question.firstPlayerChoice:
		curr_question.firstPlayerChoice = playerChoice
		curr_question.save()
		return JsonResponse({"status": "wait"})
	else:
		if str(curr_question.firstPlayerChoice) == str(playerChoice):
			secondaryImage = SecondaryImage.objects.get(id=playerChoice)
			secondaryImage.score = F('score') + 1
			secondaryImage.save()
			randomPrimaryImage = PrimaryImage.objects.order_by('?').first()
			new_question = Question(game=curr_question.game, primaryImage=randomPrimaryImage)
			new_question.save()
			curr_question.delete()
			return JsonResponse({"status": "match", "newQuestion": new_question.id})
		else:
			curr_question.firstPlayerChoice = None
			curr_question.save()
			return JsonResponse({"status": "fail"})
			
def ajax_get_question(request, questionId):
	pass
			