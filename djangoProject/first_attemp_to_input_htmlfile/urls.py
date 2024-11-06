from django.shortcuts import HttpResponse,render
from django.urls import path
from first_attemp_to_input_htmlfile import views
app_name = 'first_attempt_to_input_htmlfile'


urlpatterns=[
    path('',views.index,name="index"),
    path('index2',views.index2,name="index2")
]