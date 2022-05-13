from django.contrib import admin
from .models import Blog, BlogComment


class BlogAdmin(admin.ModelAdmin):
    """ Allow admin users to manage blog posts """
    list_display = (
        'blog_title',
        'blog_content',
        'author',
        'image',
        'date_created',
    )
    ordering = ['-date_created']


class BlogCommentAdmin(admin.ModelAdmin):
    """ Allow admin users to manage user comments """
    list_display = (
        'blog',
        'blog_comment',
        'author',
        'date_added',
    )
    ordering = ['-date_added']


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
