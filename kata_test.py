#!/usr/bin/env python

import unittest
from kata import Kata
	
class KataTests(unittest.TestCase):
	def setUp(self):
		self.kata = Kata()
	
	def test_kata(self):        		
		self.assertEquals(1, 1)

if __name__ == '__main__':
	unittest.main()