#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
#import simplejson as json
import json
import sys

class YoudaoDic():
    """
    Youdao dictionary API
    """
    VERSION = 1.1

    URL = 'http://fanyi.youdao.com/openapi.do'

    KEY_FROM = 'Dic-EVE'

    KEY = '975360059'

    TYPE = 'data'

    # 可选值xml, json
    DOC_TYPE = 'json'

    def translate(self, text):
        """
        Translation method，transmit word to server，return result
        """
        # 参数
        params = {'keyfrom': self.KEY_FROM, 'key': self.KEY, 'type': self.TYPE, 'doctype': self.DOC_TYPE, 'version': self.VERSION ,'q': text}
        request = urllib2.urlopen(self.URL, urllib.urlencode(params))
        data = request.read()
        return json.loads(data)

    def format_for_command(self, text):
        """
        Format the translation result
        """
        data = main(text)
        # TODO：格式化字符串
        if data:
            print 'Youdao translation:'
            print '\t Origination text:', data.get('query', text) 
            translation = data.get('translation', None) 
            if translation: 
                for t in translation:
                    print '\t Translation:', t
            else:
                'Not found that word'

def main(text):
    if text and text.strip() != '':
        return YoudaoDic().translate(text)

if __name__ == '__main__':
    if sys.argv and len(sys.argv) >= 2:
        l = sys.argv[1:]
        YoudaoDic().format_for_command(' '.join(l))
    else:
        print 'Youdao translatin： \n\t Tips：Input what you want to be translated'
