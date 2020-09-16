# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:29:30 2020

@author: SONY
"""

import unittest
import sys

sys.path.insert(1, 'C:\Windows\System32\cmd.exe')

import check_tb
from check_tb import check1

class Testdata(unittest.TestCase):
       # def integrated1(self):
          #  s1 = 'tganachari@gmail.com'
          # s2 = 'switchon'
           # if s1== a :
             #   print("Pass")
           # else:
              #  print("fail")
                
        def testvalue(self):
            print("Test case 1")
            self.assertEqual(check1('tejashwini@gmail.com','switchon'),1)
            
                        
        def testvalue1(self):
            print("Test case 2")
            self.assertEqual(check1('tejashwini@gmail.com','swit'),0) 
        
        def testvalue2(self):
            print("Test case 3")
            self.assertEqual(check1('tejashwini@switchon.com','switchon'),0)
            
        def testvalue3(self):
            print("Test case 4")
            self.assertEqual(check1('tejashwini@g.com','switchon'),0)
       
        def testvalue4(self):
            print("Test case 5")
            self.assertEqual(check1('tejashwini@gmail.com','switchon'),0)
            
if __name__ == '__main__':
    unittest.main()