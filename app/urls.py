from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("create-post/", CreatePostView.as_view(), name="create-post"),
]
