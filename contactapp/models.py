from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class Country(models.Model):
	"""Field Name"""
	country_name = models.CharField(max_length=30)

	class META:
		verbose_name_plural = "Countery"

	def __str__(self):
		return self.country_name
			

class State(models.Model):
	"""Field Name"""
	state_name = models.CharField(max_length=30)
	country_name = models.ForeignKey('Country',verbose_name="Countery",on_delete=models.PROTECT)

	class META:
		verbose_name_plural = "States"

	def __str__(self):
		return self.state_name

class City(models.Model):
	"""Field Name"""
	city_name = models.CharField(max_length=30)
	state_name = models.ForeignKey('State',verbose_name="States",on_delete=models.PROTECT)
	country_name = models.ForeignKey('Country',verbose_name="Countery",on_delete=models.PROTECT)

	class META:
		verbose_name_plural = "City"

	def __str__(self):
		return self.city_name


class contact_list(models.Model):
	"""Field Name"""
	c_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20)
	number = models.CharField(max_length=20)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	image = models.ImageField(upload_to='profile_image/',blank=True)

	class META:
		verbose_name_plural = "contact_list"

	def delete(self,*args,**kwargs):
		self.image.delete()
		super().delete(*args,**kwargs)

