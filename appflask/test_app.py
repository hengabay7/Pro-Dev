
import unittest
from flask import Flask

class SimpleTest(unittest.TestCase):
    def test_success(self):
        print("✅ Test passed successfully!")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()