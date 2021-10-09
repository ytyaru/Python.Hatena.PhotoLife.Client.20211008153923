#!/usr/bin/env python3
# coding: utf8
import requests
class ResponseParser:
    def parse(self, res:requests.Response):
        if res.ok: self.parse_success(res)
        else: self.parse_fail(res)
    def parse_success(self, res:requests.Response):
        print(res.text)
    def parse_fail(self, res:requests.Response):
        print('[ERROR] リクエストに失敗しました。HTTPステータスコードが200〜400以外です。', file=sys.stderr)
        print(res.status_code, file=sys.stderr)
        print(res.text, file=sys.stderr)
        print(res)
        res.raise_for_status()

