'''
Created on Jan 30, 2015

@author: AlirezaF
'''
import unittest
from statics.Utils import *
from random import * 

class Test(unittest.TestCase):


    def test_MD5(self):
        self.assertEqual(get_md5("alireza"), "d41d8cd98f00b204e9800998ecf8427e",
                          "md5 not working on 'alireza' test")


    def test_unique_randoms(self):
        self.assertEqual(len(set(sample(range(0, 10), 10))), 10, "not unique randoms")    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMD5']
    unittest.main()