# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    res = HttpResponse('hello world')
    return res


def hello_with_template(request):
    return render(request, 'hello.html')

