from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def deal(request):
    return HttpResponse('Сделки')
def tasks(request):
    return HttpResponse('Задачи')
def calendar(request):
    return HttpResponse('Планировщик')