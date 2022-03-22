from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="homepage"),
    path('all/', views.AllPosts.as_view(), name="all-posts"),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post-details"),
    path('about/', views.about, name="about-page"),
    path('help/', views.help, name="help-page"),
    path('new_post/', views.new_post, name="new-post")
]