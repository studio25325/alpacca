from django.shortcuts import render
from .models import Menu
from django.utils import timezone
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView,
)

# Create your views here.
def ajax(request):
    return render(request, 'menu/post_list.html')


class TestView(TemplateView):
    model = Menu
    template_name = "menu/post_list.html"
    now = timezone.localtime(timezone.now())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["foo"] = self.now.year
        context["menu"] = Menu.objects.all()

        return context

    #Ajax読み込み処理
    def more(request):
        return render(request, 'menu/show.html')
