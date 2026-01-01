from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import Blog,Category,Comment
from django.db.models import Q

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
        # 'category':category,
    }
    return render(req,'posts_by_category.html',context)

def blogs(req,slug):
    single_blog = get_object_or_404(Blog,slug=slug, status='Published')
    if req.method == 'POST':
        comment = Comment()
        comment.user = req.user
        comment.blog = single_blog
        comment.comment = req.POST['comment']
        comment.save()
        return HttpResponseRedirect(req.path_info) # jya comment submit karo aej page par rahiye 
    
    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comments_count = comments.count()
    context = {
        'single_blog': single_blog,
        'comments':comments,
        'comments_count' : comments_count,
    }
    return render(req,'blogs.html',context)

def search(req):
    keyword = req.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q (short_description__icontains=keyword) | Q (blog_body__icontains=keyword) | Q(title__icontains=keyword) , status='Published')  # icontains i means caseinsensitive 
    context ={
        'blogs':blogs,
        'keyword': keyword,
    }
    
    return render(req,'search.html',context)