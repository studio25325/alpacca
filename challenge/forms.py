from django import forms

from .models import Post10




class Post10Form(forms.ModelForm):

    CHOICE_1 = (
        ('1', '大凱'),
        ('2', '有希'),
    )
    CHOICE_2 = (
        ('ストローク', 'ストローク'),
        ('サーブ', 'サーブ'),
        ('腹筋', '腹筋'),
    )

    """定数リストによるプルダウンメニュー"""
    challenger = forms.ChoiceField(widget=forms.Select, choices=CHOICE_1)
    title = forms.ChoiceField(widget=forms.Select, choices=CHOICE_2)

    class Meta:
        model = Post10
        fields = ('title', 'result', 'challenger', 'created_date',)
