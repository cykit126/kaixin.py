﻿# coding: utf-8

from .events import Events
import unittest

class Subscriber(object):
    def __init__(self,v=0):
        self.x = v

    def __call__(self,**args):
        self.x += args['y']

class EventsTest(unittest.TestCase):

    def setUp(self):
        self._events = Events()

    def test_add_subscriber(self):
        sub1 = Subscriber()
        sub2 = Subscriber()
        self._events.add_subscriber("test",sub1)
        self._events.add_subscriber("test",sub2)
        self._events.fire_event("test",y=2)
        self.assertEqual(2,sub1.x)
        self.assertEqual(2,sub2.x)

    def test_remove_subscriber(self):
        sub1 = Subscriber()
        self._events.add_subscriber("test",sub1)
        self._events.remove_subscriber("test",sub1)
        self._events.fire_event("test",y=2)
        self.assertEqual(0,sub1.x)