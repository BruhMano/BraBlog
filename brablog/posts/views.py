from django.shortcuts import render,redirect
from .models import Post
from django.core.paginator import Paginator
from like.models import Like
from users.forms import NewPostForm


def index(request):
        likes = Like.objects.all()
        post_list = Post.objects.order_by('-pub_date').all()
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
        paginator = Paginator(post_list, 6)  # показывать по 6 записей на странице.
        page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
        page = paginator.get_page(page_number)  # получить записи с нужным смещением
        return render(request,'index.html',{'page': page, 'paginator': paginator})

def fav(request):
        likes = Like.objects.all()
        post_list = Post.objects.order_by('-pub_date').all()
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
        paginator = Paginator(post_list, 6)  # показывать по 6 записей на странице.
        page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
        page = paginator.get_page(page_number)  # получить записи с нужным смещением
        return render(request,'favorites.html',{'page': page, 'paginator': paginator})

def post(request,postname):
        likes = Like.objects.all()
        post = Post.objects.get(title=postname)
        post.likes = Like.objects.filter(post=post).all().__len__()
        try:
                like = Like.objects.get(post=post,user=request.user)
        except Exception as e:
                like = None
        if like in likes:
                post.is_liked_by_current_user = True
        else:
                post.is_liked_by_current_user = False
        return render(request,'posty.html',{'post': post})


def newpost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.is_liked_by_current_user = False
            post.likes = 0
            post.save()
            return redirect('index')
        return render(request, "newpost.html",{"form": form})
    form = NewPostForm()
    return render(request, "newpost.html",{"form": form})
