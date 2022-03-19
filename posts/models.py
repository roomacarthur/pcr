from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

class Review(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Rreview")
    review = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    votes = models.ManyToManyField(User, related_name="Review_likes", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    