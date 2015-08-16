from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^wait$', views.setup_game, name='wait_game'),
	url(r'^start$', views.start_game, name='start_game')
]