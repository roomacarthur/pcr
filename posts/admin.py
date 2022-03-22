from django.contrib import admin
from .models import Post, Review


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ("updated_on", "created_on")
    list_display = ("title", "author", "created_on", "updated_on")
    search_fields = ["author", "title", "content"]

admin.site.register(Post, PostAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_filter = ("updated_on", "created_on")
    list_display = ("name", "created_on")
    search_fields = ["name", "review"]

admin.site.register(Review, ReviewAdmin)