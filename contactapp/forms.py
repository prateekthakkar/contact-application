from django import forms
from .models import *

country=[(' ', ' '),
		 ('India','India'),
		 ('U.S','U.S'),]

state=[	(' ', ' '),
		 ('Gujarat','Gujarat'),
		 ('Delhi','Delhi'),]

city=[(' ', ' '),
		('Patan','Patan'),
		 ('Surat','Surat'),
		 ('Ahmedabad','Ahmedabad'),]

class contact_form(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}),required=True,max_length=20)
	number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Number'}),required=True,max_length=20)
	country = forms.ChoiceField(choices=country)
	state = forms.ChoiceField(choices=state)
	city = forms.ChoiceField(choices=city)
	class Meta():
		model = contact_list
		fields = ['name','number','country','state','city','image']
