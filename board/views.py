from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post

# Create your views here.

def home(request):
    message = ''
    if request.session.get('message', False):
        message = request.session['message']
        del request.session['message']
    try :   #모든 게시글을 가져오기
        posts = Post.objects.all()
        paginator = Paginator(posts, 5)  # 페이지 5개씩 찍어냄 Show 25 contacts per page
        page = request.GET.get('page')
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
        message = "더이상 게시글이 존재하지 않습니다."
    except:
        message = "게시글이 존재하지 않습니다."
    context = {'message':message, 'contacts':contacts}
    return render(request, 'board/home.html', context)

def board_view(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}
    return render(request, 'board/board_view.html', context)

def board_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect(reverse('home'))

def board_update(request):
    post = Post.objects.get(pk=request.POST.get('pk'))
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.author = request.POST.get('author')
    post.save()

    context = {"post":post, 'site':"post"}
    return render(request, "board/board_view.html", context)
    

def board_create(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        password = request.POST.get('password')
        post = Post(
            author = author,
            title = title,
            content = content,
            password = password,
        )
        post.save()
        return render(request, 'board/home.html')

    return render(request, 'board/new_board.html')

def check_password(request):
    password = request.POST.get('password')
    pk = request.POST.get('pk')
    post = Post.objects.get(pk=pk)
    if post.password == password:
        print("인증되었습니다")
        url = request.POST.get('url')
        if url == 'board/':
            return redirect('/board/delete/{}'.format(pk))
    else:
        message="password error"
        url='board/board_view.html'
    
    context = {'post':post, 'pk':pk}
    return render(request, url, context)