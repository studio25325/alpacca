import datetime
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
from challenge.models import Post10
from . import mixins
from django.utils import timezone

#dataFrameの利用に必要
from django_pandas.io import read_frame

import calendar
from django.utils import timezone

now = timezone.localtime(timezone.now())


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


class ShowDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post


class WeekView(mixins.WeekWithScheduleMixin, TemplateView):
    template_name = "blog/new_week.html"
    now = timezone.localtime(timezone.now())
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["week"] = Post.objects.order_by('created_date').reverse().filter(show_flag='1')
        #context["week"] = Post.objects.filter(date = self.now - datetime.timedelta(days=3))
        #↑日付指定でのデータ取得方法
        #これで日付をずらしてデータを取得できた。
        #今日の日付を中心にdfかリストにappendしてデータを制作？
        df = Post.objects.all()
        df = read_frame(df)
        context["set"] = len(df)

        #カレンダーデータ
        #today = datetime.datetime.now()
        context["today"] = self.now.month
        cal = calendar.Calendar(firstweekday=6)
        #context["calendar"] = cal.itermonthdays2(this_today.year,this_today.month)
        context["calendar"] = cal.itermonthdays2(2019,7)


        return context
