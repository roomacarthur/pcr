from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Homepage.</h1>")

def all_posts(request):
    return HttpResponse("<h1>All Posts</h1>")

def post_details(request):
    return HttpResponse("<h1>Post Details</h1>")

def user_profile(request):
    return HttpResponse("<h1>Profile</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def help(request):
    return HttpResponse("<h1>Help Page</h1>")