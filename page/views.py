from django.shortcuts import render
from django import views
from django.http import HttpResponse


def HomeView(request):
    return render(request, "home.html")
