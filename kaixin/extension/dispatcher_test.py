# coding: utf-8

from dispatcher import UrlMapper
import unittest
from kaixin.extension.dispatcher import PluginMapper

class TestingHandler1(object):
    pass
class TestingHandler2(object):
    pass
class TestingHandler3(object):
    pass

class UrlMapperTest(unittest.TestCase):

    def setUp(self):
        self._mapper = UrlMapper()

    def test_add_url(self):
        self.assertTrue(self._mapper.add_url('/test1',TestingHandler1()))
        self.assertFalse(self._mapper.add_url(None,TestingHandler1()))
        self.assertFalse(self._mapper.add_url(0,TestingHandler1()))
        self.assertFalse(self._mapper.add_url('/test2',None))

    def test_call(self):
        self.assertTrue(self._mapper.add_url('/test1',TestingHandler1()))
        self.assertTrue(self._mapper.add_url('/test2',TestingHandler2()))
        self.assertTrue(self._mapper.add_url('/test3/',TestingHandler3()))

        handler,params = self._mapper('/test1')
        self.assertIsInstance(handler,TestingHandler1)
        self.assertEqual([],params)

        handler,params = self._mapper('/test2')
        self.assertIsInstance(handler,TestingHandler2)
        self.assertEqual([],params)

        handler,params = self._mapper('/test1/arg1/arg2/')
        self.assertIsInstance(handler,TestingHandler1)
        self.assertEqual(['arg1','arg2'],params)

        handler,params = self._mapper('/none')
        self.assertIs(handler,None)
        self.assertEqual([],params)

        handler,params = self._mapper('/test3')
        self.assertIs(handler,None)
        self.assertEqual([],params)

        handler,params = self._mapper('/test3/arg1/arg2/arg3')
        self.assertIsInstance(handler,TestingHandler3)
        self.assertEqual(['arg1','arg2','arg3'],params)


class PluginMapperTest(unittest.TestCase):
    def test_basic(self):
        mapper = PluginMapper()
        (plugin,action,params) = mapper('/plugin/action/param1/param2')
        self.assertEqual('plugin',plugin)
        self.assertEqual('action',action)
        self.assertEqual(['param1','param2'],params)





























