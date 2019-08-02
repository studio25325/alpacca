from django.shortcuts import render

from django.http import HttpResponse

import urllib.request, urllib.error
from bs4 import BeautifulSoup


def index(request):

    # アクセスするURL
    url = "http://www.nikkei.com/"

    # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
    html = urllib.request.urlopen(url=url)
    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")
    # タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
    title_tag = soup.title
    # 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
    title = title_tag.string

    params = {
        'foo': 'Hi Django!',
        'title': title,
    }

    #return HttpResponse("Hello Django world!")
    return render(request, 'collect/collect.html', params)
