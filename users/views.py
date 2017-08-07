from django.http.response import HttpResponse


def index(request):
    return HttpResponse("<h1>This is a user screen</h1>")
