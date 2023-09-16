from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator


def welcome(request):
    return render(request,"network/welcome.html")
@login_required(login_url='login')
def index(request,pageno):
    objects=[post.post for post in likes.objects.filter(Liked_by=request.user) ]
    x=Post.objects.order_by("-date").all()
    p=Paginator(x,10)

    return render(request, "network/index.html",{
        'posts': p.page(pageno).object_list,'liked_by':objects,'p':p,'pageno':pageno
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
            return HttpResponseRedirect(reverse("index",args=[1]))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index",args=[1]))


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
        f=Post(post_content=content,post_owner=request.user,date=datetime.datetime.now())
        f.save()
        likes(post=f,)
        return HttpResponseRedirect(reverse('index',args=[1]))
    if request.method=="GET":
        return render(request,'network/newpost.html')
def profile(request,id):
    if request.method=="GET":
        profile_owner=User.objects.get(id=id)
        posts=Post.objects.filter(post_owner=profile_owner)
        return render(request,'network/profile.html',{
            'posts':posts,"id":id ,'followers':profile_owner.followers.all(),'following':profile_owner.following.all(),'f_l':len(profile_owner.followers.all()),'fly_l':len(profile_owner.following.all()),'profile':profile_owner
        })

        


def like(request,postid,pageno):
    if request.method=="POST":
        if request.POST.get('like'):
            post=Post.objects.get(id=postid)
            post.Liked_by.add(request.user)
            
            return HttpResponseRedirect(reverse('index',args=[pageno]))

            
        if request.POST.get('unlike'):
            post=Post.objects.get(id=postid)
            
            post.Liked_by.remove(request.user)
            return HttpResponseRedirect(reverse('index',args=[pageno]))
            
        
def follow_unfollow(request,id):
    if request.method=="POST":
        if request.POST.get('follow'):
            profile_owner=User.objects.get(id=id)
            profile_owner.followers.add(request.user)
            request.user.following.add(profile_owner)
            return HttpResponseRedirect(reverse('profile',args=[id]))

        else :
            profile_owner=User.objects.get(id=id)
            profile_owner.followers.remove(request.user)
            request.user.following.remove(profile_owner)
            return HttpResponseRedirect(reverse('profile',args=[id]))
            


def following_post(request,pageno):
    if request.method=='GET':
        p_l=[]
        list_following=request.user.following.all()
        for i in list_following:
            for j in Post.objects.order_by('-date').filter(post_owner=i):
                p_l.append(j)
        p=Paginator(p_l,10)  
        return render(request,'network/followingPost.html',{
            'follow':p.page(pageno).object_list,'p':p,'pageno':pageno
        })