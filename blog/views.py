from django.shortcuts import render

# Create your views here.

def all_blogs(request):
    """ A view to render the blogs page """
    return render(request, 'blog/blogs.html')
