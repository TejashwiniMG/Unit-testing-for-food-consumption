# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:29:30 2020

@author: SONY
"""

import unittest
import sys

sys.path.insert(1, 'C:\Windows\System32\cmd.exe')

import check
from check import check1

class Testdata(unittest.TestCase):
       # def integrated1(self):
          #  s1 = 'tganachari@gmail.com'
          # s2 = 'switchon'
           # if s1== a :
             #   print("Pass")
           # else:
              #  print("fail")
                
        def testvalue(self):
            self.assertEqual(check1('tejashwini@gmail.com','switchon'),1)
            
            
        def testvalue1(self):
            self.assertEqual(check1('tejashwini@gmail.com','swit'),0) 
        
        def testvalue2(self):
            self.assertEqual(check1('tejashwini@switchon.com','switchon'),0)# with self.assertRaises(TypeError):# check that s.split fails when the separator is not a string
            
if __name__ == '__main__':
    unittest.main()