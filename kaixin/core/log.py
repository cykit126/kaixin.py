# coding: utf-8

from logging import Handler

class StringHandler(Handler):

    def __init__(self):
        self._value = ''
        Handler.__init__(self)

    def emit(self, record):
        msg = self.format(record)
        self._value = self._value + msg
        
    def get_value(self):
        return self._value
        
    def clear_value(self):
        self._value = ''

class RecorderHandler(Handler):

    def __init__(self):
        self._records = []
        Handler.__init__(self)
    
    def get_records(self):
        return self._records
        
    def clear(self):
        return self._records
    
    def emit(self, record):
        self._records.append(record)

