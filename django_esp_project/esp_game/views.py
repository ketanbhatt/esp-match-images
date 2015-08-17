from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.db.models import F
from .models import *

import requests 


socketURL = settings.SOCKET_URL

def index(request):
	return render(request, 'esp_game/index.html', {'home': True})

def start_game(request):
	print "start_game"
	old_game = Game.objects.filter(players=1).first()
	if old_game:
		print "old_game"
		old_game.players = F('players') + 1
		old_game.save()
		randomPrimaryImage = PrimaryImage.objects.order_by('?').first()
		firstQuestion = Question(game=old_game, primaryImage=randomPrimaryImage)
		firstQuestion.save()
		context = {
			'status': 'paired',
			'heading': 'Lets Play!',
			'game': old_game,
			'question': firstQuestion,
			'socketURL': socketURL
		}
		return render(request, 'esp_game/start.html', context)
	else:
		print "new_game"
		new_game = Game()
		new_game.save()
		context = {
			'heading': 'Waiting for Opponent to join',
			'game': new_game,
			'socketURL': socketURL
		}
		return render(request, 'esp_game/start.html', context)

def game_disconnected(request, game_id):
	print "game_disconnected"
	game = get_object_or_404(Game, pk=game_id)
	question = Question.objects.filter(game=game)
	question.delete()
	game.delete()
	return render(request, 'esp_game/disconnect.html')

def ajax_submit_choice(request):
	print "ajax_submit_choice"
	questionId = request.POST.get('questionId')
	playerChoice = request.POST.get('playerChoice')
	curr_question = Question.objects.get(id=questionId)

	if not curr_question.firstPlayerChoice:
		print "added_choice"
		curr_question.firstPlayerChoice = playerChoice
		curr_question.save()
		return JsonResponse({"status": "wait"})
	else:
		if str(curr_question.firstPlayerChoice) == str(playerChoice):
			print "choice matched"
			secondaryImage = SecondaryImage.objects.get(id=playerChoice)
			secondaryImage.score = F('score') + 1
			secondaryImage.save()
			randomPrimaryImage = PrimaryImage.objects.order_by('?').first()
			new_question = Question(game=curr_question.game, primaryImage=randomPrimaryImage)
			new_question.save()
			curr_question.delete()
			return JsonResponse({"status": "match", "newQuestion": new_question.id})
		else:
			print "choice did not match"
			curr_question.firstPlayerChoice = None
			curr_question.save()
			return JsonResponse({"status": "fail"})
			
def ajax_get_question(request, question_id):
	print "getting question"
	question = get_object_or_404(Question, pk=question_id)
	question_json = {
		'game': question.game.id,
		'primaryImage': question.primaryImage.url,
		'secondaryImage1': [question.secondaryImage1.id, question.secondaryImage1.url],
		'secondaryImage2': [question.secondaryImage2.id, question.secondaryImage2.url],
		'secondaryImage3': [question.secondaryImage3.id, question.secondaryImage3.url],
		'id': question.id
	}
	return JsonResponse({"question": question_json})