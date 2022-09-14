from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def familiares(request):
    
    familiar = familiares(name ='Daniel', edad=52, fechaNac='1971,05,24')

    familiar.save()

    return HTTPResponse(f'Estoy guardando un familiar de nombre: {familiar.name}')


