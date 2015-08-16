from django.contrib import admin
from .models import PrimaryImage, SecondaryImage

class SecondaryImageInline(admin.TabularInline):
	model = SecondaryImage
	extra = 3

class PrimaryImageAdmin(admin.ModelAdmin):
	inlines = [SecondaryImageInline]


admin.site.register(PrimaryImage, PrimaryImageAdmin)
admin.site.register(SecondaryImage)
