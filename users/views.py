from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from accounts.models import User
from products.models import Product
from django.views.decorators.http import require_POST, require_http_methods


@login_required
@require_http_methods(["GET"])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    products = user.like_products.all()
    context = {
        'member': user,
        'products':products
    }
    return render(request, "users/profile.html", context)


@login_required
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


@login_required
@require_POST
def follow(request, member_pk):
    member = get_object_or_404(User, pk=member_pk)
    if member != request.user:
        if member.followers.filter(pk=request.user.pk).exists():
            member.followers.remove(request.user)
        else:
            member.followers.add(request.user)
    return redirect("users:profile", username=member.username)