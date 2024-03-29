# Welcome to my First Django App

I am creating this app by refering https://docs.djangoproject.com/en/2.2/intro/tutorial01/

## Prerequisites

1. Install Python ( https://www.python.org/downloads/ )
2. Install Django ( `pip install django` ) make sure you run powershell/cmd in administrator mode.

## Getting Started

👉 **To Create Project**

`django-admin startproject mysite`

👉 **To Create Polls App**

`python manage.py startapp polls`

##W

1. **Update The View**

go to file `polls\views.py`

```py
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

```

2. **Create Polls URL**

`polls\url.py`

```py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

3. **Update Root URL**

`mysite\urls.py`

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

```

4. **Run the Server**

   `python manage.py runserver`

   go to url `http://localhost:8000/polls/`

   ![My app running](https://github.com/rupeshtiwari/django-first-app/blob/master/docs/my%20first%20app%20running.PNG)
