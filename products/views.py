from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from accounts.models import User
from .models import Product, Comment
from .forms import ProductForm, CommentForm
from django.views.decorators.http import require_POST, require_http_methods



@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        product = Product.objects.create(user=request.user, title=title, content=content)
        return redirect("products:detail", product.pk)
    return render(request, "products/create.html",)


@require_http_methods(["GET", "POST"])
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comment_set.all().order_by("-pk")
    context = {
        'product' : product,
        'comments' : comments,
    }
    return render(request, "products/detail.html", context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.title = request.POST["title"]
        product.content = request.POST["content"]
        product.save()
        context = {'product' : product}
        return redirect("products:detail", product.pk)
    context = {'product' : product}
    return render(request, "products/update.html", context)


@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('home')



@require_POST
def create_comment(request, pk):
    product = get_object_or_404(Product, pk=pk)
    content = request.POST["content"]
    comment = Comment.objects.create(user=request.user, product=product, content=content)
    comment.save()
    return redirect("products:detail", product.pk)

@require_POST
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product = comment.product
    comment.delete()
    return redirect("products:detail", product.pk)

@require_POST
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product = comment.product
    comment.content = request.POST["content"]
    comment.save()
    return redirect('products:detail', product.pk)