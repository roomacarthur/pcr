from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPosts.as_view(), name="homepage"),
    path('about/', views.about, name="about-page"),
    path('help/', views.help, name="help-page"),
    path('new_post/', views.NewPost.as_view(), name="new-post"),
    path('new_review/', views.NewReview.as_view(), name="new-review"),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post-details"),
    path('<str:slug>/edit/', views.PostEdit.as_view(), name="edit-post"),
    path('<str:slug>/delete/', views.PostDelete.as_view(), name="delete-post"),
    path(
        '<int:pk>/delete-review/',
        views.ReviewDelete.as_view(), name="delete-review"),
    path(
        'edit-review/<int:pk>',
        views.ReviewEdit.as_view(), name="edit-review"),
    path('like/<str:pk>/', views.LikeView, name="like-post"),
    path('vote/<str:pk>/', views.ReviewLikeView, name="like-review"),
]
