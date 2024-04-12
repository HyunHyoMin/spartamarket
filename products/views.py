from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Users
from django.views.decorators.http import require_POST, require_http_methods



@require_http_methods(["GET"])
def detail(request):
    return render(request, "products/detail.html")
