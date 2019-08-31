from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
	name = models.CharField(max_length = 120)
	age = models.IntegerField()
	available = models.BooleanField(default = True)
	image = models.ImageField()
	price = models.DecimalField(max_digits = 5, decimal_places = 2)

	def __str__ (self):
		return self.name