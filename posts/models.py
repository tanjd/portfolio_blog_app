from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=200, unique=True)
#     description = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)

#     def _str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("home")

#     class Meta:
#         verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # categories = models.ManyToManyField(
    #     Category, blank=True, null=True, through="CategoryToPost"
    # )
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def _str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


# class CategoryToPost(models.Model):
#     post = models.ForeignKey(Post)
#     category = models.ForeignKey(Category)
