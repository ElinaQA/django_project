from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def courses(request):
    return HttpResponse('Разные курсы')
def lessons(request):
    return HttpResponse('Твои уроки')
def chat(request):
    return HttpResponse('Чат')