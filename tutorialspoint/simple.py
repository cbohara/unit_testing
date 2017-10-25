#!/usr/bin/env python
import unittest2
from unittest2 import TestCase

def add(x, y):
    return x + y

class SimpleTest(TestCase):
    def testadd1(self):
        self.assertEquals(add(4,5),9)

if __name__ == "__main__":
    unittest2.main()
