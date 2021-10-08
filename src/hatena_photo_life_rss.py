#!/usr/bin/env python3
# coding: utf8
import feedparser
import urllib.parse
import pprint
import os
from base64 import b64encode
import requests
import mimetypes
import xmltodict
import pathlib
from path import Path
# フォルダの公開範囲を「トップと同じ」にしないとRSSに反映されない
# https://f.hatena.ne.jp/ytyaru/%E6%97%A5%E6%9C%AC%E8%AA%9E/rss?page=1
# はてなフォトライフAtomAPIのFeedUriはトップフォルダのみ。RSSのURLを直接操作したほうが応用できる。
class HatenaPhotoLifeRss:
    def __init__(self, hatena_id):
        self.__hatena_id = hatena_id
    def get(self, folder:str='Hatena Blog', page:int=1):
        folder = f'/{urllib.parse.quote(folder)}' if folder else ''
#        url = f'https://f.hatena.ne.jp/{self.__hatena_id}{folder}/rss'
        url = f'https://f.hatena.ne.jp/{self.__hatena_id}{folder}/rss?page={page}'
#        url = f'https://f.hatena.ne.jp/{self.__hatena_id}{folder}/rss'
#        url = 'https://f.hatena.ne.jp/ytyaru/cli/rss'
#        url = 'https://f.hatena.ne.jp/ytyaru/Hatena%20Blog/rss'
        print(url)
        feed = feedparser.parse(url)
        pprint.pprint(feed, depth=1)
#        pprint.pprint(feed['feed'])
        pprint.pprint(len(feed['entries']))
#        pprint.pprint(feed['entries'])
        print()
#        print(feed)

if __name__ == '__main__':
    rss = HatenaPhotoLifeRss('ytyaru')
    rss.get()
