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
                "value": "DjangoでWebからポストした",
            }],
        "image_url": files
      }]
})



import pandas as pd


#Ajaxの使い方
def index(request):
    import socket
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    title = 0
    params = {
        'foo': 'Hi Django!',
        'title': 'title',
        'host': 'host',
        'ip': 'ip',
    }
    params['foo'] = files
    params['host'] = host
    params['ip'] = ip

    return render(request, 'coin/index.html', params)


def slack(request):
    #slackにポスト
    #pythonanywhereでは通らない様子
    requests.post(s_url, data)
    return render(request, 'coin/slack.html')



def more(request):
    return render(request, 'coin/more.html')
