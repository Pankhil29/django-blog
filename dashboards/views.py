from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render,redirect
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogPostForm,AddUserForm,EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


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
    if not req.user.is_staff:
        return HttpResponseForbidden("Admins only")
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
    if not req.user.is_staff:
        return HttpResponseForbidden("Admins only")
    category = get_object_or_404(Category,pk=pk)
    if req.method == 'POST':
        form = CategoryForm(req.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category) # means ke category me je data hoy aene form me put karo
    context = {
        'form': form,
        'category':category,
    }
    return render(req,'dashboard/edit_category.html',context)

def delete_category(req,pk):
    if not req.user.is_staff:
        return HttpResponseForbidden("Admins only")
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')


# Posts
def posts(req):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(req,'dashboard/posts.html',context)

def add_post(req):
    if req.method == 'POST':
        form = BlogPostForm(req.POST,req.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temporary save the data
            post.author = req.user
            # print('form valid')
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')    
        else:
            print('form is invalid')
            print(form.errors)
    form = BlogPostForm()
    context = {
        'form':form
    }
    return render(req,'dashboard/add_post.html',context)


def edit_post(req,pk):
    post = get_object_or_404(Blog,pk=pk)
    if not (req.user.is_staff or post.author == req.user):
        return HttpResponseForbidden("You are not allowed")
    if req.method == 'POST':
        form = BlogPostForm(req.POST,req.FILES,instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)   
            form.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form' : form,
        'post':post

    }
    return render(req,'dashboard/edit_post.html',context)

def delete_post(req,pk):
    post = get_object_or_404(Blog,pk=pk)
    if not (req.user.is_staff or post.author == req.user):
        return HttpResponseForbidden("You are not allowed")
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')

# Users
def users(req):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(req,'dashboard/users.html',context)

def add_user(req):
    if req.method == 'POST':
        form = AddUserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    
    form = AddUserForm()
    context = {
        'form':form
    }
    return render(req,'dashboard/add_user.html',context)

def edit_user(req,pk):
    user = get_object_or_404(User,pk=pk)
    if req.method == "POST":
        form = EditUserForm(req.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        else :
            print(form.errors)
    form = EditUserForm(instance=user)
    context = {
        'form':form,
        # 'user':user,
    }
    return render(req,'dashboard/edit_user.html',context)

def delete_user(req,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')