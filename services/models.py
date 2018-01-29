from django.db import models
from django.contrib.auth.models import User
from address.models import Area, Address
from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save, post_delete
# Create your models here.



class Unit(models.Model):
	unit_type = models.CharField(max_length=255)

	def __str__(self):
		return self.unit_type


class Category(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(null=True, blank=True, upload_to="category_images")

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	category = models.ForeignKey(Category, on_delete="PROTECT", null=True, blank=True)
	image = models.ImageField(null=True, blank=True, upload_to="product_images")
	unit = models.ForeignKey(Unit, on_delete="PROTECT")
	price = models.DecimalField(max_digits=5, decimal_places=3, default=0)
	area = models.ManyToManyField(Area)

	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# return reverse("category_products", kwargs={"category_name":self.category})

def create_user_profile(sender, instance, created, **kwargs):
	send_mail('Welcome onboard '+ instance.username,
	'we are looking forward to helping you get your home fixed '+ instance.username +'. thank you for signing up',
	'projects@home.villa-nuova.com',
	[instance.email])
post_save.connect(create_user_profile, sender=User, dispatch_uid="create_user_profile")

