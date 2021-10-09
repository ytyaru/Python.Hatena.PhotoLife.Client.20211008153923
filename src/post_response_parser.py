#!/usr/bin/env python3
# coding: utf8
import requests
import xmltodict
import re
import ResponseParser from response_parser
class PostResponseParser(ResponseParser):
    def parse_success(self, res:requests.Response):
        xml = xmltodict.parse(res.text)
#       print(xml['entry']['dc:subject']['#text'])
#       print(xml['entry']['generator']['#text'])
        print(xml['entry']['hatena:imageurl'])
        print(xml['entry']['hatena:imageurlsmall'])
        print(xml['entry']['hatena:syntax'])
        print(self._get_image_id(xml['entry']['hatena:syntax']))
        print(self._get_image_datetime(xml['entry']['hatena:syntax']))
    def _get_image_id(self, hatena_syntax):
        return re.search(r'([0-9]{14,}[pjg]):image$', xml['entry']['hatena:syntax']).group(1)
    def _get_image_datetime(self, hatena_syntax):
        return re.search(r'([0-9]{14,})[pjg]:image$', xml['entry']['hatena:syntax']).group(1)
