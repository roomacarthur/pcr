from django.contrib import admin
from .models import Post, Review
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('review')