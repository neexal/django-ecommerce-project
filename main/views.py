from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import generic

# Create your views here.
def home(request):
	context = {
		 'products': Product.objects.all(),
		 'category' : Category.objects.all()
	}
	return render(request, 'main/index.html', context)


def product_details(request, id):
	context = {
		'product_details' : Product.objects.get(pk = id)
	}
	return render(request, 'main/product_details.html', context)

def category(request):
	context = {
	'category' : Category.objects.all()
	}
	return render(request, 'main/category.html', context)

def category_items(request, id):
	context = {
		'category_name' : Category.objects.get(pk = id),
		'category_items' : Product.objects.filter(category=id)

	}
	return render(request, 'main/category_items.html', context)

def search(request):
	query = request.GET['query']
	context ={
		# 'category_name' : Product.objects.all(),
		'category_items' : Product.objects.filter(title__icontains=query)
	}
	return render(request, 'main/search.html', context)