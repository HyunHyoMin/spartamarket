from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User
from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        nickname = request.POST["nickname"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            user = User.objects.create_user(username=username, nickname=nickname, password=password)
            auth_login(request, user)
        return redirect("home")
    return render(request, "accounts/signup.html")


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('home')


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        return redirect("home")
    return render(request, "accounts/login.html")


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('home')


@require_http_methods(["GET"])
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user,
    }
    return render(request, "accounts/profile.html", context)


@require_POST
def update_profile_image(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.image = request.FILES["image"]
    user.save()
    return redirect("accounts:profile", user.pk)