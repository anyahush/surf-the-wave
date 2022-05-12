from django.shortcuts import render, get_object_or_404

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


def blog_detail(request, blog_id):
    """ A view to display individual blog posts """

    blog = get_object_or_404(Blog, pk=blog_id)

    template = 'products/product_detail.html'
    context = {
        'blog': blog,
    }

    return render(request, template, context)
