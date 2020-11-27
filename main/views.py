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
		'category_items' : Category.objects.get(id=id).item_set.all()

	}
	return render(request, 'main/category_items.html', context)

# class DetailView(generic.DetailView):
#     model = Products
#     template_name = 'main/category_items.html'