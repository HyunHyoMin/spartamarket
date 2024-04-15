from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, LoginForm
from django.views.decorators.http import require_POST, require_http_methods


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
        return redirect("home")
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, "accounts/signup.html", context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('home')


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get("next") or "home"
            return redirect(next_url)
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, "accounts/login.html", context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('home')