from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    return render(request, "network/index.html",{
        'posts': Post.objects.all(),'liked_by':[post.post for post in likes.objects.filter(Liked_by=request.user) ]
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def newpost(request):
    if request.method=="POST":
        data=request.POST
        content=data['content']
        f=Post(post_content=content,post_owner=request.user)
        f.save()
        likes(post=f,)
        return HttpResponseRedirect(reverse('index'))
    if request.method=="GET":
        return render(request,'network/newpost.html')
def profile(request,id):
    if request.method=="GET":
        profile_owner=User.objects.get(id=id)
        posts=Post.objects.filter(post_owner=profile_owner)
        return render(request,'network/profile.html',{
            'posts':posts
        })

        


def like(request,postid):
    if request.method=="GET":
        if not likes.objects.filter(post=Post.objects.get(id=postid),Liked_by=request.user):
            post=Post.objects.get(id=postid)
            f=likes(post=post,Liked_by=request.user)
            f.save()
            return HttpResponseRedirect(reverse('index'))

            
        else:
            post=Post.objects.get(id=postid)
            
            likes.objects.get(post=post,Liked_by=request.user).delete()
            return HttpResponseRedirect(reverse('index'))
            
        
        