# coding: utf-8

__author__ = 'Wilbur Luo'

from const import Const

STATUS = Const()
STATUS._200 = '200 OK'
STATUS._301 = '301 Moved Permanently'
STATUS._302 = '302 Moved Temporarily'
STATUS._304 = '304 Not Modified'
STATUS._403 = '403 Forbidden'
STATUS._404 = '404 Not Found'
STATUS._500 = '500 Internal Server Error'

FORMAT_STRING = Const()
FORMAT_STRING.rfc_datetime = "%a, %d-%b-%Y %H:%M:%S GMT"

from datetime import datetime
from datetime import timedelta

def get_past_time():
    return get_datetime_delta(days=-100)

def get_datetime_delta(**options):
    return (datetime.utcnow() + timedelta(**options)).strftime(FORMAT_STRING.rfc_datetime)
