import os
import unittest
import datetime

if not "CONFIG_PATH" in os.environ:
    os.environ["CONFIG_PATH"] = "blog.config.TestingConfig"

import blog
from blog.filters import *

class FilterTests(unittest.TestCase):
    def testDateFormat(self):
        date = datetime.date(1999, 12, 31)
        formatted = dateformat(date, "%y/%m/%d")
        self.assertEqual(formatted, "99/12/31")

    def testDateFormatNone(self):
        formatted = dateformat(None, "%y/%m/%d")
        self.assertEqual(formatted, None)

if __name__ == "__main__":
    unittest.main()
