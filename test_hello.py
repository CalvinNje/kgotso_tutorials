import io
from unicodedata import name
import unittest
import unittest.mock

import HelloWorld


class TestHelloWorld(unittest.TestCase):

    def test_level_one(self):
        name = "HelloWorld"
        strings = "Don't forget quote mark when working with strings."
        output = name, strings
        self.assertEqual(HelloWorld.first_code(), (name,strings))
   
if __name__ == '__main__':
    unittest.main()