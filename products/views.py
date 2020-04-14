from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def description(request):
    description = get_object_or_404(Product)
    return render(request, "description.html", {"description": description})
