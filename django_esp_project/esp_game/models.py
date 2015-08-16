from django.db import models

class BaseImage(models.Model):
	url = models.URLField()

	def __unicode__(self):
		return self.url
		
	class Meta:
		abstract = True

class PrimaryImage(BaseImage):
	pass

class SecondaryImage(BaseImage):
	primaryImage = models.ForeignKey(PrimaryImage)
	score = models.IntegerField(default=0)

