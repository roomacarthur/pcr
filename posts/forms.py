from .models import Post, Review
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "live_link", "repo_link",)
        
class ReviewForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ("body",)