from django.shortcuts import render, get_object_or_404
from blog.models import post

def blog_view(request):
    posts = post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    single_post = get_object_or_404(post, id=pid)
    context = {'post': single_post}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    posts = post.objects.all()
    context = {
        'posts': posts,
        'name': 'ilia',
        'last_name': 'haghani'
    }
    return render(request, 'ilia/test.html', context)

# blog/views.py
from django.shortcuts import render
from .models import post

def blog_view(request):
    posts = post.objects.filter(status=True)
    latest_posts = post.objects.filter(status=True).order_by("-publishd_date")[:4]

    return render(request, "blog/blog-home.html", {
        "posts": posts,
        "latest_posts": latest_posts,
    })
