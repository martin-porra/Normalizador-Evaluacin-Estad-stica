from django.shortcuts import render
from django.http import HttpResponse

def upload(request):
    return HttpResponse("Pagina de subida de archivos")
