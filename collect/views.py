from django.shortcuts import render

from django.http import HttpResponse

import urllib.request, urllib.error
from urllib.request import urlopen
import urllib.request
import sys
from bs4 import BeautifulSoup


def index(request):

    html = urlopen("https://news.yahoo.co.jp/").read()

    soup = BeautifulSoup(html, 'html.parser')

    title = []
    u = []

    # print(soup.prettify())
    # jQueryと同じにセレクターを書く
    elements = soup.select(".topicsList li.topicsListItem a")
    for element in elements:
        title = element.text
        u = element.get("href")
        print("title: " + element.text + ", href: " + element.get("href"))


    params = {
        'foo': 'Hi Django!',
        'title': title,
        'url': u,
    }

    #return HttpResponse("Hello Django world!")
    return render(request, 'collect/collect.html', params)
