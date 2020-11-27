from django.db import models

# Create your models here.
class Category(models.Model):
	category = models.CharField(max_length=30)
	category_image = models.ImageField(blank = True, null = True)
	def __str__(self):
		return self.category

	class Meta:
		verbose_name_plural = 'categories'


class Product(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField()
	price = models.PositiveIntegerField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, null = True)

	def __str__(self):
		return self.title 

	def delete(self, *args, **kwargs):
		self.image.delete()
		super().delete(*args, **kwargs)	


