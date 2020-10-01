from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse
from .models import Product, Category
# Create your views here.

def home(request, category_slug=None):
	category_page = None
	products = None
	if category_slug != None:
		category_page = get_object_or_404(Category,slug=category_slug)
		products = Product.objects.filter(category= category_page, available=True)

	else :
		products = Product.objects.all().filter(available = True)

	context = {
		'category' : category_page,
		'products' : products
	}
	return render(request,'home.html',context)




def productPage(request):
	return render(request,'product.html',{})