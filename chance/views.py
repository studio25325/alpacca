from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, resolve_url
from django.http import HttpResponse
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from .models import CMatch
from .models import CGame
from django.utils import timezone
now = timezone.localtime(timezone.now())

#会員情報関連
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
User = get_user_model()

#dataFrameの利用に必要
from django_pandas.io import read_frame

from .forms import (
    MatchForm, GameForm,
)


#非ログイン対応
class OnlyYouMixin(UserPassesTestMixin):
    """本人か、スタッフユーザーだけアクセスを許可する"""
    raise_exception = False

    def test_func(self):
        user = self.request.user
        #return user.is_superuser
        return user.is_staff


#メイン画面
class MainView(OnlyYouMixin, TemplateView):
    model = CMatch
    template_name = "chance/index.html"
    now = timezone.localtime(timezone.now())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = self.now

        context["foo"] = 10

        #リスト表示
        context["posts"] = CMatch.objects.reverse().order_by('created_date')[:10]

        return context


#試合登録フォーム
class MatchCreateView(OnlyYouMixin, CreateView):
    model = CMatch
    template_name = "chance/match_new.html"
    form_class = MatchForm

    def get_success_url(self):
        return resolve_url('chance:match_view')


#試合詳細
class MatchView(OnlyYouMixin, CreateView):
    model = CMatch
    template_name = "chance/match_view.html"
    form_class = GameForm
    now = timezone.localtime(timezone.now())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #直近登録の試合情報を取得
        #set = CMatch.objects.filter(title='a').filter(show_flag='1')
        set = CMatch.objects.all().last()
        #当該試合のIDを取得
        over_id = set.id

        #当該試合のゲーム数をカウント
        show_game = CGame.objects.filter(game_id = over_id)
        if show_game.first() is not None:
            df = read_frame(show_game)
            df_game_count1 = df[df.games == '1']
            df_game_count2 = df[df.games == '2']
            df_game_count1 = len(df_game_count1)
            df_game_count2 = len(df_game_count2)

            context["game_count1"] = df_game_count1
            context["game_count2"] = df_game_count2

            #成功率の算出
            context["probability_stroke"] = df["stroke_error"].sum() / df["stroke"].sum() * 100
            context["probability_service"] = df["service_error"].sum() / df["service"].sum() * 100
            context["probability_receive"] = df["receive_error"].sum() / df["receive"].sum() * 100
            context["probability_net"] = df["net_error"].sum() / df["net"].sum() * 100

        context["player"] = set.player
        context["opponent"] = set.opponent
        context["created_date"] = set.created_date

        context['form'] = GameForm( initial = { 'game_id':over_id } )

        return context

    def get_success_url(self):
        return resolve_url('chance:match_view')


#試合登録フォーム
class MatchDetailView(OnlyYouMixin, DetailView):
    model = CMatch
    template_name = "chance/match_detail.html"
    now = timezone.localtime(timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = self.now

        #遷移元の引数を確認
        over_id = self.kwargs['pk']
        #当該ゲーム情報
        #set = CMatch.objects.all().filter(pk = over_id)
        set = CMatch.objects.get(pk = over_id)
        context["foo"] = set.player

        #当該試合のゲーム数をカウント
        show_game = CGame.objects.filter(game_id = over_id)
        df = read_frame(show_game)


        df_game_count1 = df[df.games == '1']
        df_game_count2 = df[df.games == '2']
        df_game_count1 = len(df_game_count1)
        df_game_count2 = len(df_game_count2)

        context["player"] = set.player
        context["opponent"] = set.opponent
        context["created_date"] = set.created_date
        context["game_count1"] = df_game_count1
        context["game_count2"] = df_game_count2

        #成功率の算出
        context["probability_stroke"] = df["stroke_error"].sum() / df["stroke"].sum() * 100
        context["probability_service"] = df["service_error"].sum() / df["service"].sum() * 100
        context["probability_receive"] = df["receive_error"].sum() / df["receive"].sum() * 100
        context["probability_net"] = df["net_error"].sum() / df["net"].sum() * 100


        return context
