from django.shortcuts import get_object_or_404, render,redirect
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm


@login_required(login_url='login')
def dashboard(req):
    category_count = Category.objects.all().count()
    # print(category_count)
    blog_count = Blog.objects.all().count()
    # print(blog_count)
    context = {
        'category_count': category_count,
        'blog_count' : blog_count,
    }
    return render(req,'dashboard/dashboard.html',context)

def categories(req):
    return render(req,"dashboard/categories.html")

def add_category(req):
    if req.method == 'POST':
        form = CategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm()
    context = {
        'form' : form
    }
    return render(req,'dashboard/add_category.html',context)

def edit_category(req,pk):
    category = get_object_or_404(Category,pk=pk)
    if req.method == 'POST':
        form = CategoryForm(req.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category':category,
    }
    return render(req,'dashboard/edit_category.html',context)

def delete_category(req,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')


def posts(req):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(req,'dashboard/posts.html',context)