from django.shortcuts import HttpResponse


def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return HttpResponse("Hello, world home. You're at the polls index.")
