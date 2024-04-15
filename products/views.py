from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.core.files.storage import default_storage


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        image = request.FILES.get("image")
        product = Product.objects.create(user=request.user, title=title, content=content, image=image)
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

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.title = request.POST["title"]
        product.content = request.POST["content"]
        if "image" in request.FILES and product.image:
            default_storage.delete(product.image.path)
            product.image = request.FILES["image"]
        product.save()
        return redirect("products:detail", product.pk)
    context = {'product' : product}
    return render(request, "products/update.html", context)

@login_required
@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('home')


@login_required
@require_POST
def create_comment(request, pk):
    product = get_object_or_404(Product, pk=pk)
    content = request.POST["content"]
    comment = Comment.objects.create(user=request.user, product=product, content=content)
    comment.save()
    return redirect("products:detail", product.pk)

@login_required
@require_POST
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product = comment.product
    comment.delete()
    return redirect("products:detail", product.pk)

@login_required
@require_POST
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product = comment.product
    comment.content = request.POST["content"]
    comment.save()
    return redirect('products:detail', product.pk)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect('products:detail', product.pk)
    return redirect('accounts:login')
