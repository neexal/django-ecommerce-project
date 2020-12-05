from django.contrib import admin
from .models import Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	list_display = ('id','title', 'price','category',)
	search_fields = ('title',)
	list_display_links = ('id','title', )
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
	search_fields = ('category',)

admin.site.register(Category, CategoryAdmin)