from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Новости')
def catalog(request):
    return HttpResponse('Каталог')
def partner(raguest):
    return HttpResponse('Контрагенты')