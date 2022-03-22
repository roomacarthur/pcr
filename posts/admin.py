from django.contrib import admin
from .models import Post, Review


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ("updated_on", "created_on", "approved")
    list_display = ("title", "author", "created_on", "updated_on", "approved")
    search_fields = ["author", "title", "content"]
    actions = ["approve_posts", "unapprove_posts"]

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)
    
    def unapprove_posts(self, request, queryset):
        queryset.update(approved=False)

admin.site.register(Post, PostAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_filter = ("updated_on", "created_on", "approved")
    list_display = ("name", "created_on", "approved")
    search_fields = ["name", "review"]
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=False)

admin.site.register(Review, ReviewAdmin)