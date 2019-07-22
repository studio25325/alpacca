from django import forms

from .models import Post




class BlogForm(forms.ModelForm):

    CHOICE_1 = (
        ('1', '家族のみ'),
        ('2', '全員表示'),
    )
    CHOICE_2 = (
        ('1', '非対応'),
        ('2', '予約済'),
    )

    """定数リストによるプルダウンメニュー"""
    show_flag = forms.ChoiceField(widget=forms.Select, choices=CHOICE_1)
    reservation_flag = forms.ChoiceField(widget=forms.Select, choices=CHOICE_2)

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'show_flag', 'reservation_flag', 'start_time', 'end_time', 'date',)
