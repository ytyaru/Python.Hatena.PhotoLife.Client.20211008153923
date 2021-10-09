#!/usr/bin/env python3
# coding: utf8
import sys
import argparse
import requests
import response_parser from ResponseParser
import hatena_photo_life_rss from HatenaPhotoLife
import wsse from WSSE
class CLI:
    def __init__(self):
        self.VERSION = '0.0.1'
    def parse():
        parser = self._make_parser()
        args = parser.parse_args()
        print(args, file=sys.stderr)
        self._cli_routing(args)
    def _cli_routing(self, args):
        if self._not_found_sub_commands(args): self._not_found_sub_commands_exec()
        else: self._found_sub_commands_exec(args)
    def _not_found_sub_commands(self, args): return not hasattr(args, 'handler')
    def _not_found_sub_commands_exec(self, args):
        parser.print_help()
        sys.exit(1)
    def _found_sub_commands_exec(self, args):
        # APIクライアント生成
        api = HatenaPhotoLife(
                WSSE.from_json(
                    Path.here('secret.json'),
                    Path.here('secret-schema.json')))
        # 実行する
        args.handler(args, api)
    def _make_parser(self):
        parser = argparse.ArgumentParser(description=f'画像をアップロードする。はてなフォトライフへ。	{self.VERSION}')
        sub = parser.add_subparsers()
        # post
        parser_post = sub.add_parser('post', help='アップロードする。`post -h`')
        parser_post.add_argument('path', help='画像ファイルパス')
        parser_post.add_argument('-t', '--title', help='画像のタイトル（初期値＝pathのファイル名）')
        parser_post.add_argument('-f', '--folder', help='アップロード先のフォルダ名')
        parser_post.add_argument('-g', '--generator', help='アップロードしたツール名（フォルダ振分用）')
        parser_post.add_argument('-p', '--response-parser', help='API応答パーサのパス（LinedResponseParser.py）')
        parser_post.set_defaults(handler=command_post)
        # set-title
        parser_title = sub.add_parser('set-title', help='タイトルを変更する。`set-title -h`')
        parser_title.add_argument('image_id', help='画像ID（yyyyMMddHHmmss）')
        parser_title.add_argument('title', help='タイトル')
        parser_title.set_defaults(handler=command_set_title)
        # delete
        parser_delete = sub.add_parser('delete', help='削除する。see `delete -h`')
        parser_delete.add_argument('image_id', help='画像ID（yyyyMMddHHmmss）')
        parser_delete.set_defaults(handler=command_delete)
        # get
        parser_get = sub.add_parser('get', help='取得する。`get -h`')
        parser_get.add_argument('image_id', help='画像ID（yyyyMMddHHmmss）')
        parser_get.set_defaults(handler=command_get)
        # feed
        parser_feed = sub.add_parser('feed', help='最新データをいくつか取得する。`feed -h`')
        parser_feed.set_defaults(handler=command_feed)
        return parser

class Command:
    @staticmethod
    def post(args, api):
        print('command_post', file=sys.stderr)
        res = api.post(args.path, title=args.title, folder=args.folder, generator=args.generator) 
        ResponseParser(res).parse()
    @staticmethod
    def set_title(args, api):
        print('command_set_title', file=sys.stderr)
        res = api.set_title(args.image_id, args.title) 
        ResponseParser(res).parse()
    @staticmethod
    def delete(args, api):
        print('command_delete', file=sys.stderr)
        res = api.delete(args.image_id) 
        ResponseParser(res).parse()
    @staticmethod
    def get(args, api):
        print('command_get', file=sys.stderr)
        res = api.get(args.image_id) 
        ResponseParser(res).parse()
    @staticmethod
    def feed(args, api):
        print('command_feed', file=sys.stderr)
        res = api.feed() 
        ResponseParser(res).parse()

