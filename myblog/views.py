from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
def home(request):
    return HttpResponse("Welcome to blog home")

def blog(request):
    return HttpResponse('Hello from the blog')

def blogPosts(request):

    post = Post.objects.all()
    context = {'post': post}

    return render(request, 'index.html', context)

def addPost(request):
    return render(request, 'addPost.html')

def addrec(request):
    x= request.POST['blogTitle']
    y= request.POST['blogAuthor']
    z= request.POST['body']

    post = Post(title=x, author=y, body=z)
    post.save()

    return redirect("/posts")

def updatePost(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'update.html', {'post': post})

def deletePost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("/posts")

def uprec(request, id):
    x= request.POST['blogTitle']
    y= request.POST['blogAuthor']
    z= request.POST['body']

    post = Post.objects.get(id=id)

    post.title = x
    post.author = y
    post.body = z
    post.save()

    return redirect("/posts")