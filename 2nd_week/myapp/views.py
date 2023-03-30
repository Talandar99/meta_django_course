from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1> Hello From App </h1>")


def say_hello(request):
    return HttpResponse("<h1> Say hello From App </h1>")


def menu(request):
    text = """ <h1> this is menu </h1> """
    return HttpResponse(text)
