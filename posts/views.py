from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'posts/index.html')

def all_posts(request):
    return render(request, 'posts/all_posts.html')

def post_details(request):
    return render(request, 'posts/post_details.html')

def user_profile(request):
    return render(request, 'posts/profile.html')

def about(request):
    return render(request, 'posts/about.html')

def help(request):
    return render(request, 'posts/help.html')