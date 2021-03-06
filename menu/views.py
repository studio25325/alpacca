from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, resolve_url
from .models import Menu
from django.utils import timezone
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView,
)
from .forms import (
    MenuFormEdit,
)

# Create your views here.
def ajax(request):
    return render(request, 'menu/post_list.html')

#class MainView(TemplateView):
class MainView(ListView):
    model = Menu
    template_name = "menu/post_list.html"
    now = timezone.localtime(timezone.now())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["foo"] = self.now.year
        set = Menu.objects.filter(title='a').filter(show_flag='1')
        context["list_a"] = set[0]
        #クエリーオブジェクトの扱い方
        #context["menu"] = set[1].memo
        set = Menu.objects.filter(title='b').filter(show_flag='1')
        context["list_b"] = set[0]
        set = Menu.objects.filter(title='c').filter(show_flag='1')
        context["list_add"] = set[0]
        set = Menu.objects.filter(title='d').filter(show_flag='1')
        context["menu_sat"] = set[0]
        set = Menu.objects.filter(title='e').filter(show_flag='1')
        context["menu_sun"] = set[0]
        set = Menu.objects.filter(title='f').filter(show_flag='1')
        context["menu_mon"] = set[0]
        set = Menu.objects.filter(title='g').filter(show_flag='1')
        context["menu_tue"] = set[0]
        set = Menu.objects.filter(title='h').filter(show_flag='1')
        context["menu_wed"] = set[0]
        set = Menu.objects.filter(title='i').filter(show_flag='1')
        context["menu_thu"] = set[0]
        set = Menu.objects.filter(title='j').filter(show_flag='1')
        context["menu_fri"] = set[0]
        set = Menu.objects.filter(title='k').filter(show_flag='1')
        context["refrigerator"] = set[0]
        set = Menu.objects.filter(title='l').filter(show_flag='1')
        context["freezer"] = set[0]
        set = Menu.objects.filter(title='m').filter(show_flag='1')
        context["menu_hold"] = set[0]

        return context

    #Ajax読み込み処理
    #def more(request, ):
    #    request.test = "test1"
    #    a = Menu.objects.filter(title='a').filter(show_flag='1')
    #    request.test = a[0]
    #    model = get_object_or_404(Menu, pk=1)
    #    return render(request, 'menu/show.html', )


#Ajax読み込み処理
def more(request, ):
    c = MenuUpdateView
    request.test = "test1"
    #a = Menu.objects.filter(title='a').filter(show_flag='1')
    #request.test = a[0]
    model = get_object_or_404(Menu, pk=1)

    model = Menu
    template_name = "menu/menu_edit.html"
    form_class = MenuFormEdit

    post = get_object_or_404(Menu, pk=1)
    form = MenuFormEdit(instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
    else:
        form = MenuFormEdit(instance=post)

    return render(request, 'menu/show.html', {'form' : form} )




#投稿内容の編集
class MenuUpdateView(UpdateView):
    model = Menu
    template_name = "menu/menu_edit.html"
    form_class = MenuFormEdit

    def get_success_url(self):
        return resolve_url('menu:main')
        #return redirect('menu:main')
