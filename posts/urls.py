from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="homepage"),
    path('all/', views.all_posts, name="all-posts"),
    path('posts/', views.post_details, name="post-details"),
    path('profile/', views.user_profile, name="user-profile"),
    path('about/', views.about, name="about-page"),
    path('help/', views.help, name="help-page")
]