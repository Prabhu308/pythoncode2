import unittest
import app

class TestAppFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(app.add(2, 3), 5)
        self.assertEqual(app.add(-1, 1), 0)
        self.assertEqual(app.add(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(app.multiply(2, 3), 6)
        self.assertEqual(app.multiply(-1, 1), -1)
        self.assertEqual(app.multiply(0, 10), 0)

if __name__ == '__main__':
    unittest.main()

