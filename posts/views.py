from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from urllib3 import add_stderr_logger
from .models import Post

def home(request):
    return render(request, 'posts/index.html')

# def all_posts(request):
#     return render(request, 'posts/all_posts.html')

def post_details(request):
    return render(request, 'posts/post_details.html')

def about(request):
    return render(request, 'posts/about.html')

def help(request):
    return render(request, 'posts/help.html')

def new_post(request):
    return render(request, 'posts/new_post.html')

# all posts view.
class Posts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('-created_on')
    template_name = 'posts/all_posts.html'
    paginate_by = 10
