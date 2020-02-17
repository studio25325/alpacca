from django.shortcuts import render
from django.http import HttpResponse
import urllib.request, urllib.error
from urllib.request import urlopen
import urllib.request
import sys


import requests
import re
from bs4 import BeautifulSoup

articles = []

url = 'https://news.ycombinator.com/news'

r = requests.get(url)
html_soup = BeautifulSoup(r.text, 'html.parser')

for item in html_soup.find_all('tr', class_='athing'):
    item_a = item.find('a', class_='stroylink')
    item_link = item_a.get('href') if item_a else None
    item_text = item_a.get_text(strip=True) if item_a else None
    next_row = item.find_next_sibling('tr')
    item_score = next_row.find('span', class_='score')
    item_score = item_score.get_text(strip=True) if item_score else '0 point'
    #regexを使って正しい要素を見つける
    item_comments = next_row.find('a', text = re.compile('\d+(&nbsp;|\s)comment(s?)'))
    item_comments = item_comments.get_text(strip=True).replace('\xa0', ' ') if item_comments else '0 comments'

    articles.append({'link' : item_link,
                    'title' : item_text,
                    'score' : item_score,
                    'comments' : item_comments
                    })



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
        'scr':articles,
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
