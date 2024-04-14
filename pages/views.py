from django.shortcuts import render
from products.models import Product


def home(request):
    products = Product.objects.all().order_by("-pk")
    context = {'products':products}
    return render(request, 'pages/home.html', context)
