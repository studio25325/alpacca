from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    show_flag = models.CharField('表示フラグ', max_length=50, default=1)
    reservation_flag = models.CharField('予約フラグ', max_length=50, default=1)
    #start_time = models.TimeField('開始時間', default=timezone.now)
    start_time = models.TimeField('開始時間', default='09:00')
    end_time = models.TimeField('終了時間', default='10:00')
    date = models.DateField('日付', default=timezone.now)

    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
