from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido")

def vista_html(request):
    return render(request, 'base.html', context={}) 