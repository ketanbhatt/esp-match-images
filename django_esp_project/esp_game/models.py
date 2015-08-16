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

class Game(models.Model):
	player = models.IntegerField(default=1)

class Question(models.Model):
	game = models.ForeignKey(Game)
	primaryImage = models.ForeignKey(PrimaryImage)
	firstPlayerChoice = models.IntegerField(blank=True, null=True)
	secondaryImage1 = models.ForeignKey(SecondaryImage, related_name="choice1", blank=True, null=True)
	secondaryImage2 = models.ForeignKey(SecondaryImage, related_name="choice2", blank=True, null=True)
	secondaryImage3 = models.ForeignKey(SecondaryImage, related_name="choice3", blank=True, null=True)

	def save(self, *args, **kwargs):
		secondaryImages = SecondaryImage.objects.filter(primaryImage=self.primaryImage).order_by('?')[:3]
		self.secondaryImage1, self.secondaryImage2, self.secondaryImage3 = secondaryImages
		super(Question, self).save(*args, **kwargs)