from django.db import models
import os
import random

# Create your models here.

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance,filename):
	new_filename = random.randint(1,399999999999)
	name, ext    = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "prducts/{new_filename}/{final_filename}".format(
			new_filename = new_filename,
			final_filename = final_filename
		)

#using model manager  step:1
# class ProductManager(models.Manager):
# 	def get_by_id(self,id):
# 		qs = self.get_queryset().filter(id=id)
# 		if qs.count() == 1:
# 			return qs.first()
# 		else:
# 			return None

class Product(models.Model):
	title  		= models.CharField(max_length=120)
	description = models.TextField()
	price 		= models.DecimalField(decimal_places=2,max_digits=20,default=30.50)
	image 		= models.ImageField(upload_to=upload_image_path,null=True,blank=True)
	featured	= models.BooleanField(default=False)

	#using model manager  step:2
	# objects = ProductManager()

	def __str__(self):
		return self.title