from django.shortcuts import render
from blogs.models import Category,Blog

def home(req):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Published')
    print(posts)
    # print(featured_posts)
    # print(categories)
    context = {
        'categories': categories,
        'featured_posts' : featured_posts,
        'posts' : posts,
    }
    return render(req,"home.html",context)