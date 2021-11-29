from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    ResumeView,
)

urlpatterns = [
    path("", ResumeView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("user/<str:username>/posts/", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
