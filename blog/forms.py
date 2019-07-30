from django import forms

from .models import Post

import bootstrap_datepicker_plus as datetimepicker





class BlogForm(forms.ModelForm):

    CHOICE_1 = (
        ('1', '家族のみ'),
        ('2', '全員表示'),
    )
    CHOICE_2 = (
        ('1', '要予約'),
        ('2', '予約済'),
    )

    """定数リストによるプルダウンメニュー"""
    show_flag = forms.ChoiceField(widget=forms.Select, choices=CHOICE_1)
    reservation_flag = forms.ChoiceField(widget=forms.Select, choices=CHOICE_2)
    #入力フォームを日付と時間に分割する場合
    #start_time = forms.SplitDateTimeField(label='開始時間')

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'show_flag', 'reservation_flag', 'start_time', 'end_time', 'date',)
        #fields = '__all__'
        widgets = {
            'date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            'start_time': datetimepicker.TimePickerInput(
                format='%H:%M',
                options={
                    'locale': 'ja',
                }

            ),
            'end_time': datetimepicker.TimePickerInput(
                format='%H:%M',
                options={
                    'locale': 'ja',
                }

            ),



        }
