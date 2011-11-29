# coding: utf-8

__author__ = 'Wilbur Luo'

import re

class RegexResolver(object):
    """
    RegexResolver使用正则表达式匹配url，返回注册的handler和参数。
    """
    
    def __init__(self):
        self._url_handler_map = {}
        self._keys = [] 
    
    def register_handler(self, pattern, handler):
        if type(pattern) != type(''):
            return False
        self._url_handler_map[pattern] = handler
        self._keys = sorted(self._url_handler_map.iterkeys(), cmp=lambda x,y: cmp(y,x))
        return True
    
    def dispatch(self, url):
        for regex in self._keys:
            match = re.match(regex, url)
            if match is not None:
                return [self._url_handler_map[regex], match.groupdict()]
        return None, {}


class ModulePageResolver(object):
    """
    ModulePageResolver根据/把URL分成片段并映射到对应模块。URL格式为 /module/page/params。
    """

    def __call__(self, url):
        if type(url) != type(""):
            return None, None, []
        
        segments = self._extra_params(url)
        module = 'index'
        page = 'index'
        params = []
        if len(segments[0]) > 0:
            module = segments[0]
        if len(segments) >= 2:
        	page = segments[1]
        if len(segments) >= 3:
        	params = segments[2:]
        return module, page, params


    def _extra_params(self, url):
        return url.lstrip('/').rstrip('/').split('/')
