import unittest
from app import app

class HelloNameTestCase(unittest.TestCase):
    def setUp(self):
        """ הכנת סביבה לבדיקה """
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_name(self):
        """ בדיקה שהנתיב מחזיר את הטקסט הנכון """
        response = self.app.get('/hello/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello testuser!', response.data)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(HelloNameTestCase))
