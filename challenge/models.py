from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Post10(models.Model):
    title = models.CharField(max_length=200)
    result = models.IntegerField()
    challenger = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
