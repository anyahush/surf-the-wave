from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Blog
from .forms import BlogForm


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

    template = 'blog/blog_detail.html'
    context = {
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def add_blog(request):
    """ Admin users can add a blog to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do this')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog. Please ensure the form is valid')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

