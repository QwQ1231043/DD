from django.shortcuts import render, HttpResponse

# Create your views here.
def movie_list(request):
    return HttpResponse("Hello world")
def movie_detail(request, movie_id):
    return HttpResponse("Hello world",movie_id)
def practice(request):
    judgement = 1234
    www={
        "name": "Dongyao Zheng",
        "age":20,
        "hobby":"video game",
    }
    wwww=[
        {"name":"Jason"},
        {"name":"christ"},
        {"name":"David"},
    ]
    context={
        'judgement':judgement,
        'www':www,
        'wwww':wwww,

    }
    return render(request,"practice.html",context)