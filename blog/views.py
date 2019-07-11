from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
from challenge.models import Post10


class TopPage(TemplateView):
    template_name = "blog/test.html"

    #テンプレートにデータを渡すにはget_context_dataをオーバーライド
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foo"] = "bar"
        return context


class ShowList(ListView):
    template_name = "blog/show_list.html"
    model = Post
    #1ページの表示件数
    paginate_by = 5

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

        context["bar"] = Post10.objects.all()  # 他のモデルからデータを取得
        #context["foo2"] = self.kwargs['pk']
        return context


class ShowDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post
