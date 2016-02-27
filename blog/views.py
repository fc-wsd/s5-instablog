# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def hello(request):
    res = HttpResponse('hello world')
    return res


def hello_with_template(request):
    return render(request, 'hello.html')


def list_posts(request):
    all_posts = Post.objects.all()
    return render(request, 'list_posts.html', {
        'posts': all_posts,
    })






