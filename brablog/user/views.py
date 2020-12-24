from django.shortcuts import render
from .models import User
from posts.models import Post
from django.core.paginator import Paginator
from like.models import Like

def profile(request, name):
    user = User.objects.get(username=name)
    likes = Like.objects.all()
    post_list = Post.objects.filter(author=user).order_by('-pub_date').all()
    for post in post_list:
        post.likes = Like.objects.filter(post=post).all().__len__()
        try:
            like = Like.objects.get(post=post,user=request.user)
        except Exception as e:
            like = None
        if like in likes:
            post.is_liked_by_current_user = True
        else:
            post.is_liked_by_current_user = False
    paginator = Paginator(post_list, 6)  # показывать по 10 записей на странице.
    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    return render(request,'profile.html',{'user': user,'page': page, 'paginator': paginator})

