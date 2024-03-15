from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def user_logout(request):
    if request.user:
        logout(request)
    return redirect(reverse_lazy('rent_app:main'))