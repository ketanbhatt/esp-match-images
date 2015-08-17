from django.contrib import admin
from .models import PrimaryImage, SecondaryImage, Question

class SecondaryImageInline(admin.TabularInline):
	model = SecondaryImage
	extra = 3

class PrimaryImageAdmin(admin.ModelAdmin):
	inlines = [SecondaryImageInline]

class SecondaryImageAdmin(admin.ModelAdmin):
	list_display = ('id', 'url', 'score')

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('game', 'primaryImage', 'firstPlayerChoice')

admin.site.register(PrimaryImage, PrimaryImageAdmin)
admin.site.register(SecondaryImage, SecondaryImageAdmin)
admin.site.register(Question, QuestionAdmin)