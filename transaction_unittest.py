import unittest
from Money import Transaction


class TestDateMethods(unittest.TestCase):
    def test_transaction(self):
        Transaction(15)


if __name__ == '__main__':
    unittest.main()
