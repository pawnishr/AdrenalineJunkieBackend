from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("<h1>This is the users page</h1>")
