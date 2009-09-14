from django.db import models

class Tweet(models.Model):
	batch = models.ForeignKey('Batch')
	to_user = models.CharField(max_length = 15)
	from_user = models.CharField(max_length = 15)
	profile_image_url = models.CharField(max_length = 1000)
	text = models.CharField(max_length = 140)
	source = models.CharField(max_length = 140)
	tweeted_at = models.DateTimeField()
	tweet_id = models.IntegerField()
	iso_language_code = models.CharField(max_length = 3)
	
class RetweetBot(models.Model):
	name = models.CharField(max_length = 50)
	is_active = models.BooleanField(default = True)
	
class RetweetPackage(models.Model):
	retweet_bot = models.ForeignKey('RetweetBot')
	search_package = models.ForeignKey('searcher.SearchPackage')
	
class RetweetAction(models.Model):
	retweet_bot = models.ForeignKey('RetweetBot')
	append_link = models.BooleanField(default = True)
	link = models.CharField(max_length=10000)

class Batch(models.Model):
	name = models.CharField(max_length = 50)
	is_active = models.BooleanField(default = True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Batches"
		
class BatchPackage(models.Model):
	batch = models.ForeignKey('Batch')
	search_package = models.ForeignKey('searcher.SearchPackage')
	
	def __unicode__(self):
		return self.search_package.name
	
	
	

	
