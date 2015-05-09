import unittest
from invoice_calculator import divide_pay

class InvoiceCalculatorTests(unittest.TestCase):

    def testDividedFairly(self):
        staff_pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0})
        self.assertEqual(staff_pay["Alice"], 90.0)
        self.assertEqual(staff_pay["Bob"], 90.0)
        self.assertEqual(staff_pay["Carol"], 180.0)

if __name__ == "__main__":
    unittest.main()
