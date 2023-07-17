from django.shortcuts import render
from django import views
from django.http import HttpResponse


def HomeView(request):
    return HttpResponse("<h1>Home<h1/>")
