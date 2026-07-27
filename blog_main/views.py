from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(req):
    # categories = Category.objects.all()
    featured_posts = Blog.objects.select_related('author').filter(is_featured=True,status='Published').order_by('updated_at')
    posts = Blog.objects.select_related('author').filter(is_featured=False,status='Published')
    print(featured_posts)
    print(posts)
    # print(featured_posts)
    # print(categories)
    
    # fetch about us
    try:
        about = About.objects.first()
        # in this we only use get function only because all,filter functions are give the object 
    except:
        about = None
    
    context = {
        # 'categories': categories,
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about':about,
    }
    return render(req,"home.html",context)


def register(req):
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            print("success")
            return redirect('login') 
        else: 
            print("not sucess")
            print(form.errors) 
            
    else:        
        form = RegistrationForm()
    context = {
         'form':form,
    }
    return render(req,'register.html',context)

def login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req,req.POST)  # why this is not created in forms.py because this form have only 2 fields so that 
        if form.is_valid():
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(req,user)
            return redirect('dashboard')
    form = AuthenticationForm() 
    context ={
            'form' : form,
        }
    return render(req,'login.html',context)

def logout(req):
    auth.logout(req)
    return redirect("home")