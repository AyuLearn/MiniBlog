from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {
        'post': post
    }
    return render(request, 'post.html', context)