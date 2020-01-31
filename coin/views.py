from django.shortcuts import render
from django.http import HttpResponse
import urllib.request, urllib.error
from urllib.request import urlopen
import urllib.request
import sys



#jsonをslackにpost
import requests,json
s_url = "https://hooks.slack.com/services/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"
files = "https://takenami.info/wp-content/uploads/2018/11/players_001.jpg"
data = json.dumps({
    "text": "Djangoからポスト",
    "username": "alpacca",
    "attachments": [{
        "fields": [
            {
                "title": "Alpacca System",
                "value": "Djangoからポストした",
            }],
        "image_url": files
      }]
})



import pandas as pd

#Ajaxの使い方
def index(request):

    title = 0
    params = {
        'foo': 'Hi Django!',
        'title': title,
    }

    return render(request, 'coin/index.html', params)


def slack(request):
    #slackにポスト
    requests.post(s_url, data)
    return render(request, 'coin/slack.html')



def more(request):
    return render(request, 'coin/more.html')
