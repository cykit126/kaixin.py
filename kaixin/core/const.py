# coding: utf-8

from string import Formatter

class Const(object):
    """
    Constant implementation
    """

    def __init__(self):
        self.__dict__['_attrs'] = {}

    def __setattr__(self,name,value):
        attrs = self.__dict__['_attrs']
        #print str(self._attrs)
        if attrs.has_key(name):
            attr = attrs[name]
            msg = Formatter().format("Can't rebind const 'const.{0}', set in '{1}:{2}'.", name, attr['file'], attr['line'])
            raise TypeError, msg
        import inspect
        frame = inspect.stack()[1]
        attr = {
            'value':value,
            'file':frame[1],
            'line':frame[2],
            'function':frame[3]
        }
        del frame
        attrs[name] = attr

    def __getattr__(self,name):
        attrs = self.__dict__['_attrs']
        if name in attrs:
            return attrs[name]['value']
        else:
            return None

