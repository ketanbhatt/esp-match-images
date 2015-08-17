from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^start$', views.start_game, name='start_game'),
	url(r'^disconnected/(?P<game_id>[0-9]+)/$', views.game_disconnected, name='game_disconnected'),
	url(r'^ajax_submit_choice$', views.ajax_submit_choice, name='ajax_submit_choice'),
	url(r'^ajax_get_question/(?P<question_id>[0-9]+)/$', views.ajax_get_question, name='ajax_get_question')
]