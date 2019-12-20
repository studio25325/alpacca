from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, resolve_url
import datetime
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from .models import Post
from challenge.models import Post10
from . import mixins
from django.utils import timezone

#会員情報関連
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
User = get_user_model()

#dataFrameの利用に必要
from django_pandas.io import read_frame

from .forms import (
    BlogForm, BlogFormEdit,
)

import calendar
from django.utils import timezone

now = timezone.localtime(timezone.now())


#非ログイン対応
class OnlyYouMixin(UserPassesTestMixin):
    """本人か、スタッフユーザーだけアクセスを許可する"""
    raise_exception = False

    def test_func(self):
        user = self.request.user
        #return user.is_superuser
        return user.is_staff


#メイン表示
class CalView(OnlyYouMixin, mixins.WeekWithScheduleMixin, TemplateView):
    model = Post
    template_name = "blog/cal.html"
    now = timezone.localtime(timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #曜日情報の取得
        cal = calendar.Calendar(firstweekday=6)


        context["defailt_year"] = self.now.year
        context["defailt_month"] = self.now.month

        context["next_month"] = 0

        dic_next = {}
        dic_next["year"] = self.now.year
        dic_next["month"] = self.now.month

        if self.kwargs.get('get_next_month') is None:
            context["pre_year"] = context["defailt_year"]
            context["pre_month"] = context["defailt_month"] - 1
            context["next_year"] = context["defailt_year"]
            context["next_month"] = context["defailt_month"] + 1
            context["view_month"] = self.now.month

            #曜日情報の取得
            context["calendar"] = cal.itermonthdays2(self.now.year, self.now.month)
        #次月処理
        else:
            context["view_month"] = self.kwargs.get('get_next_month')
            context["next_year"] = self.kwargs.get('get_next_year')
            context["next_month"] = self.kwargs.get('get_next_month') + 1
            dic_next["year"] = self.kwargs.get('get_next_year')
            dic_next["month"] = self.kwargs.get('get_next_month')

            if context["next_month"] == 14:
                context["next_month"] = 1
                dic_next["month"] = 1
                context["view_month"] = 1
                context["next_year"] = context["next_year"] + 1

            #曜日情報の取得
            context["calendar"] = cal.itermonthdays2(context["next_year"], dic_next["month"])

        #ユーザーグループの取得
        #グループ毎の処理を分岐させるにはget_context_dataをクラス毎に記載しておく
        if self.request.user.groups.filter(name='family').exists():
            context["foo1"] = 'family'
            context["week"] = Post.objects.order_by('created_date').reverse().filter(date__year=dic_next["year"], date__month=dic_next["month"])
        elif self.request.user.groups.filter(name='coach').exists():
            context["foo1"] = 'coach'
            context["week"] = Post.objects.order_by('created_date').reverse().filter(date__year=dic_next["year"], date__month=dic_next["month"])
        else:
            context["foo1"] = 'common'
            context["week"] = Post.objects.order_by('created_date').reverse().filter(show_flag='2').filter(date__year=dic_next["year"], date__month=dic_next["month"])

        #日付情報の取得
        context["now"] = self.now

        return context


#受け渡しテスト
class TestView(OnlyYouMixin, TemplateView):
    model = Post
    template_name = "blog/test.html"
    now = timezone.localtime(timezone.now())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["foo"] = self.now.year
        context["foo2"] = self.now.month
        #初期値
        context["get1"] = 1000

        if context["get1"] is 1000:
            context["get1"] = self.now.month
        else:
            context["get1"] = self.kwargs.get('set1') + 1

        return context



#詳細表示
class ScheduleDetailView(OnlyYouMixin, DetailView):
    model = Post
    template_name = "blog/detail.html"


#エントリーフォーム
class ScheduleCreateView(OnlyYouMixin, CreateView):
    model = Post
    template_name = "blog/blog_new.html"
    form_class = BlogForm

    def get_success_url(self):
        return resolve_url('schedule:schedule')


#投稿内容の編集
class ScheduleUpdateView(OnlyYouMixin, UpdateView):
    model = Post
    template_name = "blog/blog_edit.html"
    form_class = BlogFormEdit

    def get_success_url(self):
        return resolve_url('schedule:schedule')


#投稿の削除
class ScheduleDeleteView(OnlyYouMixin, DeleteView):
    model = Post
    template_name = "blog/blog_delete.html"

    def get_success_url(self):
        return resolve_url('schedule:schedule')
