from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    """ Creates Blog table in database """
    class Meta:
        ordering = ['-date_added']

    blog_title = models.CharField(max_length=254)
    blog_content_one = models.TextField()
    blog_content_two = models.TextField(null=True, blank=True)
    blog_content_three = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=254)
    image = models.ImageField()
    date_added = models.DateField(auto_now_add=True, editable=False, blank=False, null=False)

    def __str__(self):
        return self.blog_title


class BlogComment(models.Model):
    """ Creates BlogComment table in database """

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, related_name='blog')
    blog_comment = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date_added = models.DateField(
        auto_now_add=True, null=False, blank=False, editable=False
    )
