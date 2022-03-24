from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView
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
    template_name = 'posts/index.html'
    paginate_by = 10
# posts view for homepage

# post detail view.
# with help from  "therefor I blog"
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)

        reviews = post.reviews.filter(approved=True).order_by('created_on')
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
        reviews = post.reviews.filter(approved=True).order_by('created_on')
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
    if request.method == "POST":

        new_post_form = PostForm(data=request.POST)
        if new_post_form.is_valid():
            new_post_form.instance.author = request.user
            form = new_post_form.save(commit=False)
            form.save()
            return HttpResponseRedirect("/")

    else:
        form = PostForm()

    return render(request, "posts/new_post.html", {"form": form})


#   update post view
class UpdatePost(UpdateView):
    model = Post
    form = PostForm
    template_name = "posts/update_post.html"

    def form_valid(self, form):
        request = self.request
        post = form.save(sommit=False)
        post.title = request.POST.getlist("title")
        post.content = request.POST.getlist("content")
        post.author = request.user
        post.save()
        return HttpResponseRedirect("/")
 