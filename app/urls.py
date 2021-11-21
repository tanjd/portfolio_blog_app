from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", CreatePostView.as_view(), name="create-post"),
    path("post/edit/<int:pk>", UpdatePostView.as_view(), name="update-post"),
]
