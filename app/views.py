from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Post
from .forms import CreatePostForm, UpdatePostForm


# Create your views here.
# def home(request):
#     return render(request, "home.html", {})
class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-created"]


class PostDetailView(DetailView):
    model = Post
    template_name = "post-detail.html"


class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "create-post.html"


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "update-post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete-post.html"
    success_url = reverse_lazy("home")
