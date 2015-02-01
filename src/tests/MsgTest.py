'''
Created on Feb 2, 2015

@author: AlirezaF
'''
import unittest
from entities.Message import * 


class Test(unittest.TestCase):


    def test_msg_header(self):
        self.assertEqual(str(Message(123, 456)), "Message---123---456---", "wrong message header")

    def test_msg_header2(self):
        self.assertEqual(str(RequestVendorScrip(123, 456, 789, 100, "sdf")),
                          "RequestVendorScrip---123---456---789+++100+++sdf", "wrong message header")
        
    def test_msg_header3(self):
        self.assertEqual(str(ResponseVendorScrip(123, 456, "sdf")),
                          "ResponseVendorScrip---123---456---sdf", "wrong message header")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_msg_header']
    unittest.main()
