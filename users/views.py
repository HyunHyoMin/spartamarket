from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from accounts.models import User
from products.models import Product
from django.views.decorators.http import require_POST, require_http_methods

# Create your views here.

@require_http_methods(["GET"])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    products = user.like_products.all()
    context = {
        'user': user,
        'products':products
    }
    return render(request, "users/profile.html", context)


@require_http_methods(["GET", "POST"])
def update_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        user.content = request.POST["content"]
        if request.FILES:
            user.image = request.FILES["image"]
        user.save()
        return redirect("users:profile", user.username)
    context ={'user' : user}
    return render(request, "users/update_profile.html", context)