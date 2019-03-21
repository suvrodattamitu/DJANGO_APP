from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Product 

def product_list(request):
	queryset = Product.objects.all()
	context  = {
		'object_list': queryset
	}
	return render(request,"products/product_list.html",context)

def product_detail(request,pk):

	#using model manager see more 2 step in models
	
	# instance = Product.objects.get_by_id(pk)

	# if instance is None:
	# 	raise Http404("Product does not exists")

	qs = Product.objects.filter(id=pk)
	if qs.exists() and qs.count() == 1:
		instance = qs.first()
	else:
		raise Http404("product does not exists")

	instance = get_object_or_404(Product,pk=pk)
	context  = {
		'obj': instance
	}
	return render(request,"products/detail.html",context)
