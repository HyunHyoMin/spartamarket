from django.shortcuts import render
from django.db.models import Q, Count
from django.core.paginator import Paginator
from products.models import Product


def home(request):
    page = request.GET.get('page', '1')
    sort_option = request.GET.get('sort')
    if sort_option == 'views':
        products = Product.objects.all().order_by('-views')
    elif sort_option == 'likes':
        products = Product.objects.annotate(like_count=Count('like_users')).order_by('-like_count')
    else:
        products = Product.objects.all().order_by('-pk')
    paginator = Paginator(products, 6)
    page_obj = paginator.get_page(page)
    context = {
        'products': page_obj,   
        'page' : page   # 정렬 옵션을 선택해도 현재 페이지를 유지하기 위해
        }
    return render(request, 'pages/home.html', context)


def search(request):
    search = request.GET.get("search")
    page = request.GET.get('page', '1')
    sort_option = request.GET.get('sort')
    if search:
        products = Product.objects.filter(
            Q(title__icontains=search) | 
            Q(content__icontains=search) |
            Q(user__nickname__icontains=search)
            ).order_by("-pk")
        if sort_option == 'views':
            products.order_by("-views")
        elif sort_option == 'likes':
            products.annotate(like_count=Count('like_users')).order_by('-like_count')
    else:
        return home(request)
    paginator = Paginator(products, 6)
    page_obj = paginator.get_page(page)
    context = {
        'products': page_obj
        }
    return render(request, 'pages/home.html', context)