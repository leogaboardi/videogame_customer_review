from django.db import models

# Create your models here.
class Platform(models.Model):
	title = models.CharField(max_length = 200)
	release_date = models.DateField('Release date', blank = True)
	def __str__(self):
			return self.title

class User(models.Model):
	name = models.CharField(max_length = 200)
	def __str__(self):
		return self.name

class Game(models.Model):
	title = models.CharField(max_length = 200)
	platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True)
	publishing_year = models.DateField('Publishing year')
	cover = models.URLField(null=True)
	def __str__(self):
			return self.title

class Review(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	vote = models.IntegerField(default=1)
	review = models.CharField(max_length = 2000)
	date = models.DateField(null = True)
	def __str__(self):
		text = str(self.game)+"; " + str(self.vote)+"; " + str(self.review)
		return text

