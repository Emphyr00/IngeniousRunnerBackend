import unittest
from app.machine_learning.multiple_regression import MultipleRegression

class MultipleRegressionTest (unittest.TestCase):
    def test_run(self):
        mr = MultipleRegression()
        mr.run()
        
        self.assertTrue(True)