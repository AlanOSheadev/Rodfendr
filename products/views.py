from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Product
# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
