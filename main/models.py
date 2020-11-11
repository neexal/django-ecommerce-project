from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='main/images')
	price = models.PositiveIntegerField()

	def __str__(self):
		return self.title

	def delete(self, *args, **kwargs):
		self.image.delete()
		super().save(*args, **kwargs)	