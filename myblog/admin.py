from django.contrib import admin
from .models import Post

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display="title", "author", "body"

admin.site.register(Post, BlogAdmin)