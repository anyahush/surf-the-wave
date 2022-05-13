from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Blog, BlogComment
from .forms import BlogForm, BlogCommentForm

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
    comments = BlogComment.objects.filter(blog=blog_id)


    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment successfully added!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Something went wrong. Please ensure your form is valid')
            return redirect(reverse('blog_detail', args=[blog.id]))
    else:
        comment_form = BlogCommentForm()

    template = 'blog/blog_detail.html'
    context = {
        'blog': blog,
        'comment_form': comment_form,
        'comments': comments,
    }
    print(comments)

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


@login_required
def edit_blog(request, blog_id):
    """ Admin users can edit blogs on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do this')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog successfully updated')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to updated blog. Please ensure the form is valid')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.blog_title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Admin users can delete blogs from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have permission to do this')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog successfully deleted')
    return redirect(reverse('blogs'))

