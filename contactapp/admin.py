from django.contrib import admin
from .models import *
# Register your models here.

class Countryadmin(admin.ModelAdmin):
	list_display = ['country_name']
admin.site.register(Country,Countryadmin)

class Stateadmin(admin.ModelAdmin):
	list_display = ['state_name','country_name']
admin.site.register(State,Stateadmin)

class Cityadmin(admin.ModelAdmin):
	list_display = ['city_name','state_name','country_name']
admin.site.register(City,Cityadmin)


class contact_listadmin(admin.ModelAdmin):
	list_display = ['c_id','name','number','city','state','country','image']
admin.site.register(contact_list,contact_listadmin)