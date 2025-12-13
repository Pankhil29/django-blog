from django.shortcuts import render
from django.http import HttpResponse 
from .models import Blog

def posts_by_category(req,category_id):
    posts = Blog.objects.filter(status="Published",category=category_id)
    # context = {
    #     "posts":posts,
    # }
    return render(req,'posts_by_category.html',posts)
