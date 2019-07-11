from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    show_flag = models.CharField('表示フラグ', max_length=50, default=1)
    start_time = models.DateTimeField('開始時間', default=timezone.now)
    end_time = models.DateTimeField('終了時間', default=timezone.now)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
