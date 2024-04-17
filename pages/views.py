from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from products.models import Product


def home(request):
    page = request.GET.get('page', '1')
    product_list = Product.objects.all().order_by("-pk")
    paginator = Paginator(product_list, 6)
    page_obj = paginator.get_page(page)
    context = {'product_list': page_obj}
    return render(request, 'pages/home.html', context)


def search(request):
    search = request.GET.get("search")
    page = request.GET.get('page', '1')
    if search:
        product_list = Product.objects.filter(
            Q(title__icontains=search) | 
            Q(content__icontains=search) |
            Q(user__nickname__icontains=search)
            ).order_by("-pk")
    else:
        return home(request)
    paginator = Paginator(product_list, 6)
    page_obj = paginator.get_page(page)
    context = {'product_list': page_obj}
    return render(request, 'pages/home.html', context)