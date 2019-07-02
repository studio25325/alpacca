from django.shortcuts import render
from django.utils import timezone
from .models import Post10
from .forms import Post10Form
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.shortcuts import redirect

#dataFrameの利用に必要
from django_pandas.io import read_frame




def index(request):
    #return HttpResponse("10 サウザンド")
    #posts = Post10.objects.reverse().first()
    posts = Post10.objects.order_by('created_date').reverse()

    params = { # <- 渡したい変数を辞書型オブジェクトに格納
        'taiga_01': 'a',
        'taiga_02': 'b',
        'taiga_03': 'b',
        'taiga_01_days': 'a',
        'taiga_02_days': 'b',
        'taiga_03_days': 'b',
        'yuki_01': 'a',
        'yuki_02': 'b',
        'yuki_03': 'b',
        'yuki_01_days': 'a',
        'yuki_02_days': 'b',
        'yuki_03_days': 'b',
    }
    #form = PostForm()
    context = {'posts': posts, 'params': params, }
    #id = 1

    #df = Post10.objects.filter(challenger=id)
    df = Post10.objects.all()
    df = read_frame(df)
    df_t = df[df.challenger == '1']
    df_st = df_t[df_t.title == 'ストローク']
    df_se = df_t[df_t.title == 'サーブ']
    df_y = df[df.challenger == '2']

    #合計件数
    #params['title'] = len(df)

    params['taiga_01'] = df_st['result'].sum(axis=0)
    params['taiga_02'] = df_se['result'].sum(axis=0)
    params['taiga_01_days'] = len(df_st)
    params['taiga_02_days'] = len(df_se)
    params['yuki_01'] = df_y['result'].sum(axis=0)
    params['yuki_01_days'] = len(df_y)
    #df_net1 = df_p[df_p.winner == '0']

    return render(request, 'challenge/post_list.html', context)


def post10_detail(request, pk):
    post = get_object_or_404(Post10, pk=pk)
    return render(request, 'challenge/post_detail.html', {'post': post})


def post10_new(request):
    if request.method == "POST":
        form = Post10Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.localtime(timezone.now())
            post.save()
            return redirect('post10_detail', pk=post.pk)
    else:
        form = Post10Form()
    return render(request, 'challenge/post_edit.html', {'form': form})


def post10_edit(request, pk):
    post = get_object_or_404(Post10, pk=pk)
    if request.method == "POST":
        form = Post10Form(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.created_date = timezone.now()
            post.save()
            return redirect('post10_detail', pk=post.pk)
    else:
        form = Post10Form(instance=post)
    return render(request, 'challenge/post_edit.html', {'form': form})
