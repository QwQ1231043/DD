from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"my_template1.html")
def index2(request):
    return render(request,"my_template2.html")