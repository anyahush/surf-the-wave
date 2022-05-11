from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'blog_title',
        'blog_content',
        'author',
        'image',
        'date_created',
    )
    ordering = ['-date_created']


admin.site.register(Blog, BlogAdmin)
