# coding: utf-8

from events import Events
from const import Const
from http import STATUS
from Cookie import SimpleCookie
from Cookie import Morsel
from http import get_past_time

class Context(object):
    def __init__(self, request, response):
        self.request = request
        self.response = response
   
class Response(object):
    def __init__(self):
        self._resp_body = []
        self._resp_headers = []
        self._resp_status = STATUS._404
        
    def clear_response_body(self):
        self._resp_body = []

    def append_response_body(self, body):
        self._resp_body.append(body)

    def get_response_body(self):
        return self._resp_body        
        
    def append_response_header(self, header):
        self._resp_headers.append(header)
        
    def clear_response_headers(self):
        self._resp_headers = []

    def get_response_headers(self):
        return self._resp_headers

    def set_response_status(self, status):
        self._resp_status = status
                
    def get_response_status(self):
        return self._resp_status
        
    def delete_cookie(self, key, path):
        self.set_cookie(key=key, path=path, expires=get_past_time())
    
    def set_cookie(self, key, value=None, path='/', domain=None, secure=False, httponly=False, expires=None):
        morsel = Morsel()
        morsel.key = key
        morsel.coded_value = value
        morsel['path'] = path
        if expires:
            morsel['expires'] = expires
        if domain:
            morsel['domain'] = domain
        if secure:
            morsel['secure'] = secure
        if httponly:
            morsel['httponly'] = httponly
        self.append_response_header(('Set-Cookie', morsel.OutputString()))

class Request(object):
    def __init__(self, environ):
        self.environ = environ
        if 'HTTP_COOKIE' in environ:
            try:
                self.cookie = SimpleCookie(environ['HTTP_COOKIE'])
            except Cookie.CookieError:
                self.cookie = SimpleCookie()
        else:
            self.cookie = SimpleCookie() 
        
    def get_request_url(self):
        return self.environ['PATH_INFO']





