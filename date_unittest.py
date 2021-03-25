import unittest
from Date import Date


class TestDateMethods(unittest.TestCase):
    def test_smart_date_formats(self):
        date: Date = Date()
        date.set("2021-03-10")
        date.set("2021-03-10 20:03")
        date.set("2021-03-10 20:03 PST")
        date.set("2021-03 PST")
        date.set("2021-03-10 ")
        date.set("2021-03-10 PST")

        exception_raised = False
        try:
            date.set("43974843987")
        except ValueError:
            exception_raised = True
        self.assertTrue(exception_raised)

        exception_raised = False
        try:
            date.set("ddofufdhdofuh")
        except ValueError:
            exception_raised = True
        self.assertTrue(exception_raised)


if __name__ == '__main__':
    unittest.main()
