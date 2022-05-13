from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    """ Creates Blog table in database """
    class Meta:
        ordering = ['-date_created']

    blog_title = models.CharField(max_length=254)
    blog_content = models.TextField()
    author = models.CharField(max_length=254)
    image = models.ImageField()
    date_created = models.DateField(auto_now=False, editable=True, blank=True, null=True)

    def __str__(self):
        return self.blog_title


class BlogComment(models.Model):
    """ Creates BlogComment table in database """

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False)
    blog_comment = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date_added = models.DateField(
        auto_now_add=True, null=False, blank=False, editable=False
    )
