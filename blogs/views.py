from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse 
from .models import Blog,Category

def posts_by_category(req,category_id):
    posts = Blog.objects.filter(status="Published",category=category_id)
    # if we want to 404 error then we can use get_object_or_404
    category = get_object_or_404(Category, pk=category_id)

    # if we want to redirect to home page we use try except block if error occurs and dont want to show 404 error
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect("home")

    # category = Category.objects.get(pk=category_id)

    
    context = {
        "posts":posts,
        'category':category,
    }
    return render(req,'posts_by_category.html',context)
