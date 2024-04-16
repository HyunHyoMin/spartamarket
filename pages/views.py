from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator

def home(request):
    page = request.GET.get('page', '1')
    product_list = Product.objects.all().order_by("-pk")
    paginator = Paginator(product_list, 6)
    page_obj = paginator.get_page(page)
    context = {'product_list': page_obj}
    return render(request, 'pages/home.html', context)
