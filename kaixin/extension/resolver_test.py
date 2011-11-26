# coding: utf-8

import unittest
from resolver import ModulePageResolver
from resolver import RegexResolver


class ModulePageResolverTest(unittest.TestCase):
    def test_basic(self):
        resolver = ModulePageResolver()
        (module, page, params) = resolver('/module/page/param1/param2')
        self.assertEqual('module', module)
        self.assertEqual('page', page)
        self.assertEqual(['param1', 'param2'], params)
        
    def test_default(self):
        resolver = ModulePageResolver()
        module, page, params = resolver('/')
        self.assertEqual('index', module)
        self.assertEqual('index', page)
        self.assertEqual([], params)


def test(app):
    pass

class RegexResovlerTest(unittest.TestCase):    
    def test_simple(self):
        resolver = RegexResolver()
        self.assertTrue(resolver.add_handler("/test/(?P<id>\d+)/(?P<name>\w+)", test))
        handler, matches = resolver.dispatch("/test/1/hero")
        self.assertEqual('1', matches['id'])
        self.assertEqual('hero', matches['name'])

if __name__ == '__main__':
    unittest.main()



























