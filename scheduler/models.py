import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Schedule(models.Model):
    """Schedule"""
    summary = models.CharField('概要', max_length=50)
    description = models.TextField('詳細な説明', blank=True)
    show_flag = models.CharField('表示フラグ', max_length=50, default=1)
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.localtime(timezone.now()))

    def __str__(self):
        return self.summary
