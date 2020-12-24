from django.shortcuts import render, redirect
from posts.models import Post
from .models import Like
from user.models import User

def like_add(request,poste,usere):
    posto=Post.objects.get(title=poste)
    usero=User.objects.get(username=usere)
    try:
       lik = Like.objects.get(post=posto,user=usero)
       lik.delete()
    except Exception as e:
       like = Like(post=Post.objects.get(title=poste),user=User.objects.get(username=usere),like=True)
       like.save()
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer)
