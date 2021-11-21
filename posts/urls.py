from django.urls import path
from .views import (
    HomeView,
    PostDetailView,
    CreatePostView,
    UpdatePostView,
    DeletePostView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", CreatePostView.as_view(), name="create-post"),
    path("post/<int:pk>/edit/", UpdatePostView.as_view(), name="update-post"),
    path("post/<int:pk>/delete/", DeletePostView.as_view(), name="delete-post"),
]
