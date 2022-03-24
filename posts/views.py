from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, render
from .models import Post, Review
from .forms import PostForm, ReviewForm


def home(request):
    return render(request, 'posts/index.html')

def about(request):
    return render(request, 'posts/about.html')

def help(request):
    return render(request, 'posts/help.html')
# homepage view.

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
        reviews = Review.objects.filter(approved=True).order_by('created_on')
        likes = False
        
        if post.likes.filter(id=self.request.user.id).exists():
            likes=True
        
        return render(
            request, 'posts/post_details.html',
            {
                "post": post,
                "reviews": reviews,
                "likes": likes,
                "review_form": ReviewForm()
            },
        )
        
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        reviews = Review.objects.filter(approved=True).order_by('created_on')
        likes = False
        
        if post.likes.filter(id=self.request.user.id).exists():
            likes=True

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.post = post
            review.save()
        else:
            review_form = ReviewForm()
        
        return render(
            request, 'posts/post_details.html',
            {
                "post": post,
                "reviews": reviews,
                "likes": likes,
                "review_form": ReviewForm()
            },
        )

# allow user to submit a new post to the site.
def new_post(request):
    user = request.user.id
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.author = user
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()

    return render(request, "posts/new_post.html", {"form": form})

