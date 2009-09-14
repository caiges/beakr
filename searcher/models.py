from django.db import models
	
class SearchPackage(models.Model):
	name = models.CharField(max_length = 50)
	is_active = models.BooleanField(default = True)
	
	def __unicode__(self):
		return self.name
	
class Filter(models.Model):
	search_package = models.ForeignKey('SearchPackage')
	terms = models.CharField(max_length = 5000)
	is_keyword = models.BooleanField()
	is_tag = models.BooleanField()
	is_mention = models.BooleanField()
	is_location = models.BooleanField()
	
	def __unicode__(self):
		return self.terms