from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from app.models import Post

# Create your views here.
# def home(request):
#     return render(request, "home.html", {})
class HomeView(ListView):
    model = Post
    template_name = "home.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"


class CreatePostView(CreateView):
    model = Post
    template_name = "create-post.html"
    fields = "__all__"
