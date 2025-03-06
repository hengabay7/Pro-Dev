import subprocess
import unittest
from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'

def has_code_changed():
    result = subprocess.run(["git", "diff", "--name-only", "HEAD~1"], capture_output=True, text=True)
    changed_files = result.stdout.strip().split("\n")
    
    return "app.py" in changed_files  # מחזיר True אם app.py השתנה

class HelloNameTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_name(self):
        response = self.app.get('/hello/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello testuser!', response.data)

if __name__ == '__main__':
    if has_code_changed():
        print("\n🚀 זוהה שינוי ב-`app.py`! מבצע בדיקות אוטומטיות...\n")
        unittest.main()
    else:
        print("\n✅ לא זוהה שינוי בקובץ `app.py`. אין צורך בבדיקות.\n")
