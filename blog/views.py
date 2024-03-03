from django.shortcuts import render

def index(request):
    return render(request, "blog/index.html")

def privet(request):
    return render(request, "blog/arsen.html")
