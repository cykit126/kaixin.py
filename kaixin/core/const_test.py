# coding: utf-8

from const import Const
import unittest

class ConstTest(unittest.TestCase):

    def setUp(self):
        self._const = Const()
    
    def test_const(self):
        self._const.x = 1
        self._const.y = 2
        self.assertEqual(1,self._const.x)
        self.assertEqual(2,self._const.y)

    def test_exception(self):
        self._const.z = 1
        try:
            self._const.z = 2
        except Exception,e:
            self.assertIsInstance(e,TypeError)
