import unittest
from StringConverter import StringConverter


class TestConverter(unittest.TestCase):
    def setUp(self) -> None:
        self.Strconverter = StringConverter("привет")
        self.stroka = self.Strconverter.stroka

    def test_string(self):
        self.assertEqual(self.Strconverter.converter(), self.stroka.capitalize() + "!")


if __name__ == "__main__":
    unittest.main()
