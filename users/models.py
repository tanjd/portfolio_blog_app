from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics", default="default.jpg")
    biography = RichTextField(blank=True, null=True)
    github_link = models.CharField(max_length=255, blank=True)
    linkedIn_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if settings.DEBUG:
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                img.thumbnail((300, 300))
                img.save(self.image.path)
