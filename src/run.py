#!/usr/bin/env python3
# coding: utf8
import os, sys
import json
import jsonschema 
import argparse
import xmltodict
from path import Path
from wsse import WSSE 
from hatena_photo_life import HatenaPhotoLife
from FileReader import FileReader
VERSION='0.0.1'
def parse_command_by_argparse():
    parser = argparse.ArgumentParser(description=f'画像をアップロードする。はてなフォトライフへ。	{VERSION}')
    sub = parser.add_subparsers()
    # post
    parser_post = sub.add_parser('post', help='アップロードする。`post -h`')
    parser_post.add_argument('path', help='画像ファイルパス')
    parser_post.add_argument('-t', '--title', help='画像のタイトル（初期値＝pathのファイル名）')
    parser_post.add_argument('-f', '--folder', help='アップロード先のフォルダ名')
    parser_post.add_argument('-g', '--generator', help='アップロードしたツール名（フォルダ振分用）')
    parser_post.add_argument('-p', '--response-parser', help='API応答パーサのパス（LinedResponseParser.py）')
#    parser.add_argument('-p', '--not-parse-response', action='store_true', help='API応答をパースせず全XMLを出力する。デフォルトでは以下3つを1行おきに出力する。hatena:imageurl, hatena:imageurlsmall, hatena:syntax', type=bool, default=False)
#   parser.add_argument('-o', '--output-format', help='出力形式', default='text', choices=['text', 'xml'])
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

    args = parser.parse_args()
    print(args)
    if hasattr(args, 'handler'):
        # APIクライアント生成
        api = HatenaPhotoLife(
                WSSE.from_json(
                    Path.here('secret.json'),
                    Path.here('secret-schema.json')))
        args.handler(args, api)
    else:
        parser.print_help()

def show_error(res):
    print('[ERROR] リクエストに失敗しました。HTTPステータスコードが200〜400以外です。', file=sys.stderr)
    print(res.status_code, file=sys.stderr)
    print(res.text, file=sys.stderr)
    print(res)
    res.raise_for_status()
def command_post(args, api):
    print('command_post')
    res = api.post(args.path, title=args.title, folder=args.folder, generator=args.generator) 
    if res.ok: parse_response(res)
    else: show_error(res)
def command_set_title(args, api):
    print('command_set_title')
    res = api.set_title(args.image_id, args.title) 
    print(res)
    if res.ok: print(res.text)
    else: show_error(res)
def command_delete(args, api):
    print('command_delete')
    res = api.delete(args.image_id) 
    print(res)
    if res.ok: print(res.text)
    else: show_error(res)
def command_get(args, api):
    print('command_get')
    res = api.get(args.image_id) 
    print(res)
    if res.ok: print(res.text)
    else: show_error(res)
def command_feed(args, api):
    print('command_feed')
    res = api.feed() 
    print(res)
    if res.ok: print(res.text)
    else: show_error(res)

def parse_response(res):
    xml = xmltodict.parse(res.text)
#    print(xml['entry']['dc:subject']['#text'])
#    print(xml['entry']['generator']['#text'])
    print(xml['entry']['hatena:imageurl'])
    print(xml['entry']['hatena:imageurlsmall'])
    print(xml['entry']['hatena:syntax'])
    
def test_xml():
    xml = xmltodict.parse(FileReader.json(Path.here('test-3.xml')))
    print(xml)
    print(xml['entry']['dc:subject']['#text'])
    print(xml['entry']['generator']['#text'])
    print(xml['entry']['hatena:imageurl'])
    print(xml['entry']['hatena:imageurlsmall'])
    print(xml['entry']['hatena:syntax'])

if __name__ == '__main__':
    # コマンド解析
    args = parse_command_by_argparse()
    """
    # APIクライアント生成
    api = HatenaPhotoLife(
            WSSE.from_json(
                Path.here('secret.json'),
                Path.here('secret-schema.json')))
    # リクエスト
    res = api.post(args.path, title=args.title, folder=args.folder, generator=args.generator) 
    if res.ok:
        # レスポンスをパースする
        parse_response(res)
    else:
        # エラーを表示する
        print('[ERROR] リクエストに失敗しました。HTTPステータスコードが200〜400以外です。', file=sys.stderr)
        print(res.status_code, file=sys.stderr)
        print(res.text, file=sys.stderr)
        res.raise_for_status()
    """


