from django.shortcuts import render

def index(request):
	return render(request, 'esp_game/index.html')

def wait_game(request):
	return render(request, 'esp_game/wait_game.html')
