import unittest
from src.multiple_regression import MultipleRegression


class MultipleRegressionTest (unittest.TestCase):
    def test_run(self):
        mr = MultipleRegression()
        mr.run()
        
        self.assertTrue(True)