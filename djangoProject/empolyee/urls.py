from django.urls import path
from empolyee import views
from . import views
from empolyee import views
app_name = 'empolyee'
urlpatterns=[
    path('',views.empolyee_default,name='empolyee default'),
    path('<str:empolyee_name>',views.empolyee,name='empolyee'),
]
