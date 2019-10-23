from django import forms
from .models import CMatch
from .models import CGame

import bootstrap_datepicker_plus as datetimepicker


class MatchForm(forms.ModelForm):

    CHOICE_1 = (
        ('大凱', '大凱'),
        ('剛生', '剛生'),
    )
    CHOICE_2 = (
        ('1', 'Win'),
        ('2', 'Lose'),
    )

    """定数リストによるプルダウンメニュー"""
    #player = forms.ChoiceField(widget=forms.Select, choices=CHOICE_1)

    class Meta:
        model = CMatch
        fields = ('player', 'opponent', 'created_date',)
        #fields = '__all__'


class GameForm(forms.ModelForm):

    # bootstarap4
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


    CHOICE_1 = (
        ('大凱', '大凱'),
        ('剛生', '剛生'),
    )
    CHOICE_2 = (
        ('1', 'Win'),
        ('2', 'Lose'),
    )

    """定数リストによるプルダウンメニュー"""
    games = forms.ChoiceField(widget=forms.Select, choices=CHOICE_2)

    class Meta:
        model = CGame
        fields = ('game_id', 'stroke', 'stroke_error', 'service', 'service_error', 'second', 'second_error', 'receive', 'receive_error', 'net', 'net_error', 'games', 'created_date',)
        #fields = '__all__'
