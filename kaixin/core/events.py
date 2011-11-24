# coding: utf-8
#
# Events提供了一个事件引擎，其它组件通过调用add_subscriber来注册它想监听的事件。
# 事件按照注册顺序会一直传播下去直到某个事件监听器返回True表示事件已经被处理。
#

class Events(object):

    def __init__(self):
        self._events_subs_map = {}

    def add_listener(self, event, listener):
        """
        添加事件监听器到事件监听器链的末尾
        """
        if event not in self._events_subs_map:
            self._events_subs_map[event] = []
        listeners = self._events_subs_map[event]
        if listener not in listeners:
            listeners.append(listener)

    def remove_listener(self,event,listener):
        if event in self._events_subs_map:
            listeners = self._events_subs_map[event]
            if listener in listeners:
                listeners.remove(listener)

    def fire_event(self,event,**args):
        """
        如果某个事件监听器返回True，事件将停止继续传播。
        """
        if event in self._events_subs_map:
            subscribers = self._events_subs_map[event]
            for sub in subscribers:
                if not sub(**args):
                    return True
        return False

