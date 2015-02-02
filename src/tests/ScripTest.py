'''
Created on Feb 2, 2015

@author: AlirezaF
'''
import unittest
from entities.Scrip import Scrip
from entities.Node import *
from time import time


class Test(unittest.TestCase):

    def test_string_format(self):
        now = int(time())
        expiry = str(now + 100) 
        self.assertEqual(str(Scrip(444, 0x0000000F, 333, now + 100, 80)), "444&80&15&333&" + expiry +\
                          "&d41d8cd98f00b204e9800998ecf8427e",
                          "error in converting scrip to string")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_string_format']
    unittest.main()