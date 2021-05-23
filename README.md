# make Environment(Mac)

```
$ usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install python3
$ brew install pyenv
$ pyenv install –list
$ pyenv install 3.x.x
```

# Django Install

```
$ cd development/case
$ mkdir helloworld
$ cd helloworld
$ python3 -m venv env
$ source env/bin/activate
$ pip install django
```

# make Project

```
$ django-admin startproject helloworld
```

# make App

```
$ python manage.py startapp helloworld
```

# add Code

helloworldproject/urls.py

```
from django.contrib import admin
#includeを追加
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #追加
    path('', include('helloworldapp.urls'))
]
```

hellowordapp/urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloworldfunction),
]
```

hellowordapp/views.py

```
from django.shortcuts import render

#追加
def helloworldfunction(request):
    return render(request, 'index.html')
```

helloworld/templates/index.html

```
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

# Start
 
```
$ python manage.py migrate
$ python manage.py runserver
```

# References

https://kimoba.com/kasegu/install-python3anddjango.html
https://qiita.com/frosty/items/e545c6258672d88b7707
