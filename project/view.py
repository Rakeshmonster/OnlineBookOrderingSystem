from django.http import HttpResponse
from django.shortcuts import render

def form(request):
    data={
        "title":"form",
        "clist":"['php','python]"
    }
    return render(request, 'index.html')

# def aboutus(request):
#     return HttpResponse("Hello")

# def hello(request):
#     return HttpResponse("Hello Karan Vae.")
