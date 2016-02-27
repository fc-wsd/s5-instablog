# blog/views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Post


def hello(request):
    res = HttpResponse('hello world')
    return res


def hello_with_template(request):
    return render(request, 'hello.html')


def list_posts(request):
    all_posts = Post.objects \
            .select_related() \
            .prefetch_related() \
            .all().order_by('-pk')

    return render(request, 'list_posts.html', {
        'posts': all_posts,
    })


def view_post(request, pk):
    the_post = get_object_or_404(Post, pk=pk)

    return render(request, 'view_post.html', {
        'post': the_post,
    })





