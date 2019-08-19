from django.db import models
from django.utils import timezone

# Create your models here.
class Menu(models.Model):
    title = models.CharField('タイトル', max_length=255, default=1)
    memo = models.TextField('メモ', max_length=500, default=1)
    show_flag = models.CharField('表示フラグ', max_length=50, default=1)
    date = models.DateField('日付', default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
