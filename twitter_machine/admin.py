from django.contrib import admin
from models import *

class TweetAdmin(admin.ModelAdmin):
	pass

class RetweetPackageInline(admin.TabularInline):
	model = RetweetPackage
	
class RetweetActionInline(admin.TabularInline):
	model = RetweetAction

class RetweetBotAdmin(admin.ModelAdmin):
	inlines = ( RetweetPackageInline, RetweetActionInline, )

class BatchPackageInline(admin.TabularInline):
	model = BatchPackage

class BatchAdmin(admin.ModelAdmin):
	inlines = ( BatchPackageInline, )
	
admin.site.register(Tweet, TweetAdmin)
admin.site.register(RetweetBot, RetweetBotAdmin)
admin.site.register(Batch, BatchAdmin)