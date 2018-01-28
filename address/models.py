from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Area(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name



class Address(models.Model):
	user = models.ForeignKey(User, on_delete="PROTECT")
	name = models.CharField(max_length=120)
	area = models.ForeignKey(Area, on_delete="PROTECT")
	block = models.CharField(max_length=3)
	street = models.CharField(max_length=120)
	avenue = models.PositiveIntegerField(blank=True, null=True)
	building_number = models.PositiveIntegerField()
	floor = models.CharField(max_length=3, null=True, blank=True)
	apartment = models.CharField(max_length=5, null=True, blank=True)
	extra_directions = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name
