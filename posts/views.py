from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from django.shortcuts import get_object_or_404, render
from .models import Post

def home(request):
    return render(request, 'posts/index.html')

def post_details(request):
    return render(request, 'posts/post_details.html')

def about(request):
    return render(request, 'posts/about.html')

def help(request):
    return render(request, 'posts/help.html')

def new_post(request):
    return render(request, 'posts/new_post.html')

# all posts view, used within all_posts.html
class AllPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('-created_on')
    template_name = 'posts/all_posts.html'
    paginate_by = 10
# posts view for homepage

# post detail view.
# with help from  "therefor I blog"
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        reviews = post.reviews.filter(approved=True).order_by('-created_on')
        votes = False
        
        if post.likes.filter(id=self.request.user.id).exists():
            votes=True
        
        return render(
            request, 'posts/post_details.html',
            {
                "post": post,
                "reviews": reviews,
                "votes": votes
            },
        )
        