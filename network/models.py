from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    followers = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='following_users')
    following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers_users')
    img=models.CharField(max_length=1000,default='')

class Post(models.Model):
    post_content = models.CharField(max_length=500, default='none')
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Liked_by = models.ManyToManyField(User, blank=True, symmetrical=False, related_name='liked_by')
   
    

class likes(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    Liked_by=models.ForeignKey(User,on_delete=models.CASCADE)

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.CharField(max_length=1000)