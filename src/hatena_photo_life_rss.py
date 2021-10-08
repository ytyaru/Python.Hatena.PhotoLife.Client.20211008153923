#!/usr/bin/env python3
# coding: utf8
import os
from base64 import b64encode
import requests
import mimetypes
import xmltodict
import pathlib
from path import Path
# フォルダの公開範囲を「トップと同じ」にしないとRSSに反映されない
# https://f.hatena.ne.jp/ytyaru/%E6%97%A5%E6%9C%AC%E8%AA%9E/rss?page=1
class HatenaPhotoLifeRss:
    def __init__(self, hateha_id):
        self.__hatena_id = hatena_id
    def get(self, folder=None):
#        url = f'https://f.hatena.ne.jp/{hatena_id}/rss?page={page}'
#        url = f'https://f.hatena.ne.jp/{hatena_id}/{folder}/rss?page={page}'
