
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('newpost',views.newpost,name='newpost'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('like/<int:postid>',views.like,name="like")
]
