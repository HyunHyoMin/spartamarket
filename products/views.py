from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from accounts.models import User
from .models import Product, Comment
from django.views.decorators.http import require_POST, require_http_methods



@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Product.objects.create(user=request.user, title=title, content=content)
    return render(request, "products/create.html")


@require_http_methods(["GET", "POST"])
def detail(request, pk):
    return render(request, "products/detail.html")
