from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post, Review
from .forms import PostForm, ReviewForm


def about(request):
    return render(request, 'posts/about.html')

def help(request):
    return render(request, 'posts/help.html')
# homepage view.

# all posts view, used within all_posts.html
class AllPosts(generic.ListView):
    """
    Displays all current posts related to model: Post
    orders by decending order.
    renders on index.html template.
    """
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('-created_on')
    template_name = 'posts/index.html'

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

@method_decorator(login_required, name="dispatch")
class NewPost(CreateView):
    """
    If user is logged in:
    Stores a single post entry, related to model: Post.
    Uses Postform(forms.py) rendered on template: new_post.html
    """
    model = Post
    form_class = PostForm
    template_name = "posts/new_post.html"
    def form_valid(self, form):
        """
        Takes the current logged in username and sets it = to author.
        """
        form.instance.author = self.request.user
        return super(NewPost, self).form_valid(form)
    def get_success_url(self):
        """
        Takes the post-details url and applies the new posts Slug
        to return the user to the newly created Post.
        """
        return reverse("post-details", args=(self.object.slug,))

@method_decorator(login_required, name="dispatch")
class PostEdit(UpdateView):
    """
    If user is logged in:
    Target a single post, 
    Provide the ability to update post via PostForm.
    Form is rendered in update_post.html
    Upon successful update, user is redirected back to
    the post and prompted with a success message.
    """
    model = Post
    form_class = PostForm
    template_name = "posts/update_post.html"
    def get_success_url(self):
        """
        Returns user back to original post.
        """
        return reverse("post-details", args=(self.object.slug,))
    def form_valid(self, form):
        """
        Prompts user with a success message upon valid form post.
        """
        messages.success(self.request, "offt, nice edit you made there.")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name="dispatch")
class PostDelete(DeleteView):
    """
    If user is logged in:
    Target a single post
    Delete post from DB
    Redirect user to Homepage.
    """
    model = Post
    template_name = "posts/delete_post.html"
    success_message = "Your post was successfully deleted... For good."
    def get_object(self):
        """
        Get the slug of current object
        """
        slug = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug)
    def get_success_url(self):
        """
        Upon successfull deletion of post, return user to homepage.
        """
        return reverse('homepage')
    def delete(self, request, *args, **kwargs):
        """
        Success message to be displayed after deletion of post.
        Help from multiple stackoverflow posts.
        """
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)

@method_decorator(login_required, name="dispatch")
class NewReview(CreateView):
    """
    If user is logged in:
    Stores a single post entry, related to model: Post.
    Uses Postform(forms.py) rendered on template: new_post.html
    """
    model = Review
    form_class = ReviewForm
    template_name = "posts/new_review.html"
    def form_valid(self, form):
        """
        Takes the current logged in username and sets it = to author.
        """
        form.instance.name = self.request.user
        return super(NewReview, self).form_valid(form)
    def get_success_url(self):
        """
        Takes the post-details url and applies the new posts Slug
        to return the user to the newly created Post.
        """
        return reverse("post-details", args=(self.object.slug,))

@method_decorator(login_required, name="dispatch")
class ReviewDelete(DeleteView):
    """
    If user is logged in:
    Direct user to delete_review.html template
    User will be prompted with a message to confirm.

    """
    model = Review
    template_name = "posts/delete_review.html"
    success_message = "Your Review was successfully deleted... For good."
    success_url = "/"
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReviewDelete, self).delete(request, *args, **kwargs)
    def get_success_url(self, *args, **kwargs):
        return reverse("post-details", kwargs={"slug": self.object.post.slug})

@method_decorator(login_required, name="dispatch")
class ReviewEdit(UpdateView):
    """
    If user is logged in:
    Direct user to update_review.html template,
    displaying ReviewForm for that specific review.
    Post edited info back to the DB
    return user to post.
    display success message.
    """
    model = Review
    form_class = ReviewForm
    template_name = "posts/update_review.html"
    def form_valid(self, form):
        """
        Upon success prompt the user with a success message.
        """
        messages.success(self.request, "offt, nice edit you made there.")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self, *args, **kwargs):
        """
        Upon success returns user to the specific related post.
        """
        return reverse("post-details", kwargs={"slug": self.object.post.slug})

def LikeView(request, pk):
    """
    View to like/unlike Posts. 
    Gets post ID from Post model.
    Liked initially set to False. 
    if user id is found in likes, clicking will remove the like and set liked to False
    If user id is not found in likes, clicking will add the like and set liked to True. 
    """
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse("post-details", args=[str(pk)]))
    
def ReviewLikeView(request, pk):
    """
    View to like/unlike Reviews. 
    Gets review ID from Review model.
    Voted initially set to False. 
    if user id is found in votes, clicking will remove the like and set voted to False
    If user id is not found in votes, clicking will add the like and set voted to True. 
    """
    review = get_object_or_404(Review, id=request.POST.get("review_id"))
    voted = False
    if review.votes.filter(id=request.user.id).exists():
        review.votes.remove(request.user)
        voted = False
    else:
        review.votes.add(request.user)
        voted = True
    
    return HttpResponseRedirect(reverse("post-details", args=[str(pk)]))
    
