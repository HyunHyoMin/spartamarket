from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.core.files.storage import default_storage
from .forms import ProductForm

@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(request.user)
        return redirect("products:detail", product.pk)
    else:
        form = ProductForm
    context = {'form' : form}
    return render(request, "products/create.html", context)


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
    if product.user == request.user:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                product = form.save()
            return redirect("products:detail", product.pk)
        else:
            form = ProductForm(instance=product)
        context = {
            'form' : form,
            'product' : product
            }
    else:
        return redirect('home')
    return render(request, "products/update.html", context)


@login_required
@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.user == request.user:
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
    if comment.user == request.user:
        comment.delete()
    return redirect("products:detail", product.pk)


@login_required
@require_POST
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product = comment.product
    if comment.user == request.user:
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
