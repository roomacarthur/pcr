from django.contrib import admin
from .models import Post, Review
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    summernote_fields = ("content")
    list_filter = ("updated_on", "created_on")
    list_display = ("title", "author", "created_on", "updated_on")
    search_fields = ["author", "title", "content"]

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ("review")
    list_filter = ("updated_on", "created_on")
    list_display = ("name", "created_on")
    search_fields = ["name", "review"]