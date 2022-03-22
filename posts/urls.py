from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="homepage"),
    path('all/', views.Posts.as_view(), name="all-posts"),
    path('posts/', views.post_details, name="post-details"),
    path('about/', views.about, name="about-page"),
    path('help/', views.help, name="help-page"),
    path('new_post/', views.new_post, name="new-post")
]