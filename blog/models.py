from django.db import models

# Create your models here.


class Blog(models.Model):
    """ Creates Blog table in database """
    class Meta:
        ordering = ['-date_created']

    blog_title = models.CharField(max_length=254)
    blog_content = models.TextField()
    author = models.CharField(max_length=254)
    image = models.ImageField()
    date_created = models.DateTimeField()

    def __str__(self):
        return self.blog_title

