# Welcome to my First Django App

## Commands that I executed

To Create Project

`django-admin startproject mysite`

To Create Polls App

`python manage.py startapp polls`

## Update the Polls app

1. Update The View

go to file `polls\views.py`

```py
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

```

2. Create URL
