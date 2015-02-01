'''
Created on Feb 2, 2015

@author: AlirezaF
'''
import unittest
from entities.Node import *

class Test(unittest.TestCase):

    n = Node(None, 666)

    def testProcessMsg(self):
        self.assertEqual(self.n.process_msg("fake---123---456---sdfk,--sdf"),
                          {"type": "fake", "sender": "123", "receiver": "456", "data":"sdfk,--sdf"},
                           "error in parsing msg")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testProcessMsg']
    unittest.main()