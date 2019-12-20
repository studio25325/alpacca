from django.shortcuts import render
from django.utils import timezone
from .models import Post10
from .forms import Post10Form
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, resolve_url

#dataFrameの利用に必要
from django_pandas.io import read_frame

#会員情報関連
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
User = get_user_model()

#テンプレート書式関連
from django.template.loader import get_template
from django.views import generic
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from .forms import (
    Post10Form,
)

#非ログイン対応
class OnlyYouMixin(UserPassesTestMixin):
    """本人か、スーパーユーザーだけユーザーページアクセスを許可する"""
    raise_exception = False

    def test_func(self):
        user = self.request.user
        return user.is_superuser


class TopPage(OnlyYouMixin, generic.TemplateView):
    template_name = 'challenge/post_list.html'

    #テンプレートに値を渡すにはcontextをオーバー
    def get_context_data(self, **kwargs):
        context_user = super().get_context_data(**kwargs)
        #ログインユーザーのID表示
        context_user["foo"] = self.request.user.id
        context_user["foo_user"] = self.request.user
        #context_user = self.request.user
        if self.request.user.id == None:
            context_user["foo"] = 0
            #return redirect("http://127.0.0.1:8000")
        else:
            context_user["foo"] = 1

        posts = Post10.objects.order_by('created_date').reverse()[:15]
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

        context = {'posts': posts, 'params': params, 'context_user': context_user, }

        df = Post10.objects.all()
        df = read_frame(df)
        df_t = df[df.challenger == '1']
        df_st = df_t[df_t.title == 'ストローク']
        df_se = df_t[df_t.title == 'サーブ']
        df_y = df[df.challenger == '2']

        params['taiga_01'] = df_st['result'].sum(axis=0)
        params['taiga_02'] = df_se['result'].sum(axis=0)
        params['taiga_01_days'] = len(df_st)
        params['taiga_02_days'] = len(df_se)
        params['yuki_01'] = df_y['result'].sum(axis=0)
        params['yuki_01_days'] = len(df_y)

        return context


class Post10List(ListView):
    template_name = 'challenge/list.html'
    model = Post10
    context_object_name = 'post10_list'


def post10_detail(request, pk):
    post = get_object_or_404(Post10, pk=pk)
    return render(request, 'challenge/post_detail.html', {'post': post})


def post10_new(request):
    if request.method == "POST":
        form = Post10Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
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
