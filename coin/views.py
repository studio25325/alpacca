from django.shortcuts import render

from django.http import HttpResponse

import urllib.request, urllib.error
from urllib.request import urlopen
import urllib.request
import sys


import pandas as pd


def index(request):


    title = 0
    params = {
        'foo': 'Hi Django!',
        'title': title,
    }
    return render(request, 'coin/index.html', params)



def more(request):
    return render(request, 'more.html')
