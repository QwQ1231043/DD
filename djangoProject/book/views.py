from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def book_information(request, book_name):
    return HttpResponse(f"The book name is:{book_name}")
def book_default(request):
    return HttpResponse(f"Welcome to my website")

def book_id(request):
    book_id_number= request.GET.get('book_id_number')
    return HttpResponse(f"The book id is: {book_id_number}")

def author_information(request):
    context={
        'key':'value',
        'number':42,
    }
    return render(request,'my_template1.html',context)