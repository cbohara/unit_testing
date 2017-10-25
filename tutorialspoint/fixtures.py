#!/usr/bin/env python
import unittest2
from unittest2 import TestCase

class SimpleTest(TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20
        name = self.shortDescription()
        if name == "Add":
            self.a = 10
            self.b = 20
        if name == "Sub":
            self.a = 50
            self.b = 60

    def tearDown(self):
        print '\nend of test', self.shortDescription()

    def test_add(self):
        """Add"""
        result = self.a + self.b
        self.assertFalse(result == 100)

    def test_sub(self):
        """Sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)


if __name__ == "__main__":
    unittest2.main()
