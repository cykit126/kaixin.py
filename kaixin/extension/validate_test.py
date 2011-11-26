# coding: utf-8

import unittest
import validate

class ValidateTest(unittest.TestCase):
    
    def test_ipv4(self):
        self.assertTrue(validate.is_ipv4('127.0.0.1'))
        self.assertFalse(validate.is_ipv4('11'))
        self.assertFalse(validate.is_ipv4('11.11'))
        self.assertFalse(validate.is_ipv4('11.11.11')
        self.assertFalse(validate.is_ipv4('9999.12.12.12'))

if __name__ == '__main__':
    unittest.main()
