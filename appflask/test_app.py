i#!/usr/bin/env python3

import unittest

class SimpleTest(unittest.TestCase):
    def test_success(self):
        print("✅ Test passed successfully!")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()