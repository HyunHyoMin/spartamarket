from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .forms import ProfileForm
from django.views.decorators.http import require_POST, require_http_methods
from django.core.files.storage import default_storage


@require_http_methods(["GET"])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    products = user.like_products.all()
    context = {
        'member': user,
        'products': products,
    }
    return render(request, "users/profile.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def update_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        if "image" in request.FILES and user.image != 'images/default_user_image.png':
            default_storage.delete(user.image.path)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
        return redirect("users:profile", user.username)
    else:
        form = ProfileForm(instance=user)
    context = {
        'form' : form,
        'user' : user,
        }
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


@require_http_methods(["GET"])
def follower(request, member_username):
    member = get_object_or_404(User, username=member_username)
    context = {'member' : member}
    return render(request, "users/follower.html", context)


@require_http_methods(["GET"])
def following(request, member_username):
    member = get_object_or_404(User, username=member_username)
    context = {'member' : member}
    return render(request, "users/following.html", context)
