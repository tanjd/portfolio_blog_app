from django.contrib import admin
from .models import Post

# from .models import Post, Category

# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}


# admin.site.register(Post, PostAdmin)
admin.site.register(Post)
# admin.site.register(Category)
