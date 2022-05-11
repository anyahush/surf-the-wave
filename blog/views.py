from django.shortcuts import render

from .models import Blog

# Create your views here.


def blogs(request):
    """ A view to render the blogs page """

    blog = Blog.objects.all()
    template = 'blog/blogs.html'
    context = {
        'blog': blog,
    }

    return render(request, template, context)
