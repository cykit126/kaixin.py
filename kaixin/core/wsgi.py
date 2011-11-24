# coding: utf-8

from events import Events
from const import Const
from http import STATUS
import io
import logging

class Context(object):
    def __init__(self, request, response):
        self.request = request
        self.response = response
        self.events = Events()
        
class Response(object):
    def __init__(self):
        self._dispatcher = None
        self._resp_body = []
        self._resp_headers = []
        self._resp_status = STATUS._404
        
    def clear_response_body(self):
        self._resp_body = []

    def append_response_body(self, body):
        self._resp_body.append(body)
        
    def append_response_header(self, header):
        self._resp_headers.append(header)
        
    def clear_response_headers(self):
        self._resp_headers = []
        
    def set_response_status(self, status):
        self._resp_status = status
        
    def get_response_body(self):
        return self._resp_body
        
    def get_response_headers(self):
        return self._resp_headers
        

class Request(object):
    def __init__(self, environ):
        self._environ = environ
        
    def get_request_url(self):
        return self._environ['PATH_INFO']






