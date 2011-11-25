# coding: utf-8

__author__ = 'Wilbur Luo'

class RegexResolver(object):
    """
    Map url with string.
    """

    def __init__(self):
        self._url_handler_map = {}

    def add_url(self,url,handler):
        if type(url) != type(""):
            return False
        if handler is None:
            return False
        self._url_handler_map[url] = handler
        return True


    def __call__(self, url):
        if type(url) != type(""):
            return (None,None)

        params = []
        handler = None
        for item in self._url_handler_map.keys():
            hdler = self._url_handler_map[item]
            url_appended = item.rstrip('/')+'/'
            if url == item:
                handler = hdler
                break
            elif url.startswith(url_appended):
                handler = hdler
                params = url[len(url_appended):].rstrip('/').split('/')
                break
        return (handler,params)


class ModulePageResolver(object):
    """
    ModulePageResolver根据/把URL分成片段并映射到对应模块。URL格式为 /module/page/params。
    """

    def __call__(self, url):
        if type(url) != type(""):
            return (None,None,[])
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
        return (module,page,params)


    def _extra_params(self,url):
        return url.lstrip('/').rstrip('/').split('/')
