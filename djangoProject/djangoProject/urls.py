"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.urls import reverse
from book import views


def index(request):
    print(reverse("index"))
    print(reverse("book",kwargs={"book_name":"zzz"}))
    print(reverse("book"))
    print(reverse("movie:movie_list"))
    return HttpResponse("Hello world")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<book_name>', views.book_information,name="book"),
    path('index',index,name='index'),
    path('book', views.book_id, name="book"),
    path('',views.book_default,name='book'),
    path('first_attempt/', include("first_attemp_to_input_htmlfile.urls")),
    path('',views.author_information),
    path('movie/',include("movie.urls")),
    path('empolyee/',include("empolyee.urls")),

]
