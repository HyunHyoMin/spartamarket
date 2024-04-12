from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        username = request.POST["title"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        return render(request, "accounts/signup.html")
    return render(request, "accounts/signup.html")

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")


@require_POST
def logout(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('accounts:login')