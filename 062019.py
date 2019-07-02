# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:24:44 2019

@author: S534688
"""

import requests
from bs4 import BeautifulSoup

page = requests.get('https://twitter.com/hormazdsorabjee/status/1141322580831457280')
#print(page.text)
soup = BeautifulSoup(page.text, 'html5lib')
#print(soup)
spans = soup.find_all('span',{'class': 'profileTweet-actionCount'})
print(spans[0])
print(spans[0]['data-tweet-start-count'])
id = spans[0].find('span')['id']

def get_metric(span):
    number = int(span['data-tweet-start-count'])
    inner_span = span.find('span')
    span_id = inner_span['id']
    if 'reply' in span_id:
        return 'reply', number
    elif 'retweet' in span_id:
        return 'retweet', number
    elif 'likes' in span_id:
        return 'likes', number
    else:
        return None

print(get_metric(spans[0]))
print(get_metric(spans[1]))
print(get_metric(spans[2]))
