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
    def get(self, folder:str=None, page:int=1, is_sort_old:bool=False):
        folder = f'/{urllib.parse.quote(folder)}' if folder else ''
        page = f"page={page if 0 < page else 1}"
        is_sort_old = f"sort={'old' if is_sort_old else 'new'}"
        url = f'https://f.hatena.ne.jp/{self.__hatena_id}{folder}/rss?{page}&{is_sort_old}'
        res = requests.get(url)
        if res.ok: print(res.text)
        else: show_error(res)

        print('----------------')
        print(res)
        print('----------------')
        print(res.content)
        print('----------------')
        print(res.text)
        """
        print(url)
        sys.exit(1)
        feed = feedparser.parse(url)
        pprint.pprint(feed, depth=1)
#        pprint.pprint(feed['feed'])
        pprint.pprint(len(feed['entries']))
#        pprint.pprint(feed['entries'])
        print()
#        print(feed)
        """
    def _show_error(self, res):
        print('[ERROR] リクエストに失敗しました。HTTPステータスコードが200〜400以外です。', file=sys.stderr)
        print(res.status_code, file=sys.stderr)
        print(res.text, file=sys.stderr)
        print(res)
        res.raise_for_status()

if __name__ == '__main__':
    rss = HatenaPhotoLifeRss('ytyaru')
    rss.get()
#    rss.get('')
#    rss.get('Hatena Blog')
#    rss.get('日本語')
