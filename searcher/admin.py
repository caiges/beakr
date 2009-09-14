from django.contrib import admin
from models import *
	
class FilterInline(admin.TabularInline):
	model = Filter

class SearchPackageAdmin(admin.ModelAdmin):
	inlines = ( FilterInline, )
	
admin.site.register( SearchPackage, SearchPackageAdmin )

