from django.db import models
from django.utils import timezone


class Post10(models.Model):
    title = models.CharField(max_length=200)
    result = models.IntegerField()
    challenger = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.localtime(timezone.now()))

    def publish(self):
        self.created_date = timezone.localtime(timezone.now())
        self.save()

    def __str__(self):
        return self.title
