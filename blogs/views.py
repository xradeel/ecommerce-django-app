from django.shortcuts import render

def blogs(request):
    return render(request, 'blogs/blog-category.html')

def blogPost(request):
    return render(request, 'blogs/blog-post.html')
