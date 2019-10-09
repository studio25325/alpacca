from django.db import models
from django.utils import timezone


class CMatch(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='alpacca')
    player = models.CharField(max_length=100, default='大凱')
    opponent = models.CharField(max_length=100, default='対戦相手')
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.created_date.strftime("%Y/%m/%d %H:%M:%S")


class CGame(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    game_id = models.CharField(max_length=200, default=1)
    stroke = models.IntegerField(max_length=100, default=0)
    stroke_error = models.IntegerField(max_length=100, default=0)
    service = models.IntegerField(max_length=100, default=0)
    service_error = models.IntegerField(max_length=100, default=0)
    receive = models.IntegerField(max_length=100, default=0)
    receive_error = models.IntegerField(max_length=100, default=0)
    net = models.IntegerField(max_length=100, default=0)
    net_error = models.IntegerField(max_length=100, default=0)
    games = models.CharField(max_length=100, default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.game_id
