from django.shortcuts import render,HttpResponse

# Create your views here.

def empolyee_default(request):
    return HttpResponse("Welcome to empolyee website.")
def empolyee(request,empolyee_name):
    return HttpResponse("The empolyee name is", empolyee_name)
