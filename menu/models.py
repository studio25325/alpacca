from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField('タイトル', max_length=255, default=1)
    memo = models.CharField('メモ', max_length=255, default=1)

    def __str__(self):
        return self.title
