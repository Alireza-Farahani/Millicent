'''
Created on Jan 30, 2015

@author: AlirezaF
'''
import unittest
from statics.Utils import * 

class Test(unittest.TestCase):


    def testMD5(self):
        self.assertEqual(get_md5("alireza"), "d41d8cd98f00b204e9800998ecf8427e",
                          "md5 not working on 'alireza' test")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMD5']
    unittest.main()