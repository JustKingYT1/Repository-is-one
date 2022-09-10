import unittest
from StringConverter import converter


class TestConverter(unittest.TestCase):

    def test_string(self):
        self.assertEqual(converter("fsasaf"), "Fsasaf!")


if __name__ == "__main__":
    unittest.main()
