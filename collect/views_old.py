from django.shortcuts import render

from django.http import HttpResponse

import urllib.request, urllib.error
import urllib.request
import sys
from bs4 import BeautifulSoup


def index(request):

    # アクセスするURL
    url = "http://www.nikkei.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }
    request_set = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(request_set)

    # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
    #html = urllib.request.urlopen(url=url)
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


def kabuka(request):

    # アクセスするURL
    url = "http://www.nikkei.com/markets/kabu/"

    # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
    html = urllib.request.urlopen(url=url)
    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")

    # span要素全てを摘出する→全てのspan要素が配列に入ってかえされます→[<span class="m-wficon triDown"></span>, <span class="l-h...
    span = soup.find_all("span")
    # print時のエラーとならないように最初に宣言しておきます。
    nikkei_heikin = ""

    # for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
    for tag in span:
        # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
        try:
            # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
            # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
            # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
            string_ = tag.get("class").pop(0)

            # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
            if string_ in "mkc-stock_prices":
                # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
                nikkei_heikin = tag.string
                # 摘出が完了したのでfor分を抜けます
                break
        except:
            # パス→何も処理を行わない
            pass

    params = {
        'foo': 'Hi kabuka!',
        'heikin': nikkei_heikin,
    }

    #return HttpResponse("Hello Django world!")
    return render(request, 'collect/collect.html', params)
