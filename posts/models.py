from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Main Post model.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    content = models.TextField()
    live_link = models.URLField(max_length=200, blank=True)
    repo_link = models.URLField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    approved = models.BooleanField(default=True)

    # Order posts by creation date in decending order(Newest to the top.)
    class Meta:
        ordering = ["-created_on"]

    # Magic method to return a string representation of object.
    def __str__(self):
        return self.title

    # Helper to return the total count of likes on post.
    def total_likes(self):
        return self.likes.count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)

# Review Model.
class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    votes = models.ManyToManyField(User, related_name="Review_likes", blank=True)
    approved = models.BooleanField(default=True)

    # Order posts by creation date in ascending order. 
    class Meta:
        ordering = ["created_on"]

    # Helper to return an F string representation of object.
    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    