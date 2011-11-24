# coding: utf-8

__author__ = 'Wilbur Luo'

class UrlMapper(object):
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


class PluginMapper(object):
    """
    PluginMapper将URL映射到plugin。URL格式为 /plugin_name/params。
    """

    def __call__(self, url):
        if type(url) != type(""):
            return (None,None,[])
        segments = self._extra_params(url)
        plugin = segments[0]
        action = 'handle'
        params = []
        if len(segments) >= 2:
        	action = segments[1]
        if len(segments) >= 3:
        	params = segments[2:]
        return (plugin,action,params)


    def _extra_params(self,url):
        return url.lstrip('/').rstrip('/').split('/')
