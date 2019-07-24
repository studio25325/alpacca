from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, resolve_url
import datetime
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView,
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
    BlogForm,
)

import calendar
from django.utils import timezone

now = timezone.localtime(timezone.now())


#非ログイン対応
class OnlyYouMixin(UserPassesTestMixin):
    """本人か、スーパーユーザーだけユーザーページアクセスを許可する"""
    raise_exception = False

    def test_func(self):
        user = self.request.user
        return user.is_superuser



class TopPage(TemplateView):
    template_name = "blog/test.html"

    #テンプレートにデータを渡すにはget_context_dataをオーバーライド
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foo"] = "bar"
        return context


class ShowList(mixins.WeekWithScheduleMixin, TemplateView):
    template_name = "blog/week.html"
    model = Post
    #1ページの表示件数
    paginate_by = 5
    date_field = 'date'

    def get_queryset(self):
        #通常の記載
        #return Post.objects.order_by('created_date').reverse()
        #条件レコードの取得
        return Post.objects.order_by('created_date').reverse().filter(show_flag='1')
        #10件までの記載方法
        #return MyModel.objects.all()[:10]

    #他のモデルからデータ取得
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #ユーザーグループの取得
        #グループ毎の処理を分岐させるにはget_context_dataをクラス毎に記載しておく
        if self.request.user.groups.filter(name='family').exists():
            context["foo1"] = 'family'
        else:
            context["foo1"] = 'common'

        if self.request.user.id == None:
            context["foo"] = 0
        else:
            context["foo"] = 1

        #ユーザー情報の取得
        context["user"] = super().get_context_data(**kwargs)
        context["user"] = self.request.user.id
        context["user"] = self.request.user

        #グループ毎の処理を分岐させるにはget_context_dataをクラス毎に記載しておく
        if self.request.user.groups.filter(name='family').exists():
            context["user_flag"] = 'family'
        else:
            context["user_flag"] = 'common'

        context["bar"] = Post10.objects.all()[:10] # 他のモデルからデータを取得
        #context["foo2"] = self.kwargs['pk']

        #カレンダーデータの取得
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        context['week_row'] = zip(
            calendar_context['week_names'],
            calendar_context['week_days'],
            calendar_context['week_day_schedules'].values()
        )

        return context


#こいつがメイン表示
class ScheduleView(OnlyYouMixin, mixins.WeekWithScheduleMixin, TemplateView):
    template_name = "blog/schedule.html"
    now = timezone.localtime(timezone.now())
    model = Post

    def get_previous_month(self, previous_month):
        previous_month = previous_month - 1
        return previous_month
        #"""前月を返す"""
        #if date.month == 1:
        #    return date.replace(year=date.year-1, month=12, day=1)
        #else:
        #    return date.replace(month=date.month-1, day=1)

    def get_next_month(self, show_month):
        """次月を返す"""
        show_month = show_month + 1
        get_test = 6
        self.set_month = 200
        return show_month
        #if date.month == 12:
        #    return date.replace(year=date.year+1, month=1, day=1)
        #else:
        #    return date.replace(month=date.month+1, day=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["previous"] = self.get_previous_month(self.now.month)
        context["next"] = self.get_next_month(self.now.month)
        #2019/07/24 初期はないけど、再読み込みで見つかるデータを
        context["previous"] = self.set_month
        context["moo"] = self.kwargs.get('next')

        #ユーザーグループの取得
        #グループ毎の処理を分岐させるにはget_context_dataをクラス毎に記載しておく
        if self.request.user.groups.filter(name='family').exists():
            context["foo1"] = 'family'
            context["week"] = Post.objects.order_by('created_date').reverse()
        else:
            context["foo1"] = 'common'
            context["week"] = Post.objects.order_by('created_date').reverse().filter(show_flag='1')
        #context["week"] = Post.objects.filter(date = self.now - datetime.timedelta(days=3))
        #↑日付指定でのデータ取得方法
        #これで日付をずらしてデータを取得できた。
        #今日の日付を中心にdfかリストにappendしてデータを制作？
        df = Post.objects.all()
        df = read_frame(df)
        context["set"] = len(df)

        #カレンダーデータ
        context["today"] = self.now.month
        #日付情報の取得
        context["now"] = self.now

        cal = calendar.Calendar(firstweekday=6)
        #context["calendar"] = cal.itermonthdays2(this_today.year,this_today.month)
        context["calendar"] = cal.itermonthdays2(self.now.year, self.now.month)

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
    template_name = "blog/blog_new.html"
    form_class = BlogForm

    def get_success_url(self):
        return resolve_url('schedule:schedule')
