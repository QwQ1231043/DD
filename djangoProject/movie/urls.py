from django.urls import path
from . import views


app_name="movie";
urlpatterns=[
 path('list',views.movie_list, name='movie_list'),
    path('movie_detail/<int:movie_id>',views.movie_detail, name='movie_detail'),
    path('practice',views.practice, name='practice'),
]