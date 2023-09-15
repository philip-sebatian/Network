
from django.urls import path

from . import views

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path("<int:pageno>", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('newpost',views.newpost,name='newpost'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('like/<int:postid>/<int:pageno>',views.like,name="like"),
    path('follow_unfollow/<int:id>',views.follow_unfollow,name='follow_unfollow'),
    path('followingPost/<int:pageno>',views.following_post,name='followingPost')
    
]
