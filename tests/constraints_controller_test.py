import unittest
from src.block import Block
from src.field import Field
from src.constraints_controller import ConstraintsController

class ConstraintsControllerTest (unittest.TestCase):
    def test_create(self):
        block = Block()
        cc = ConstraintsController()
        
        self.assertIsInstance(cc, ConstraintsController)
        
    def test_getEntropy(self):
        block = Block()
        cc = ConstraintsController()

        self.assertEqual(cc.getEntropy(), 8)
        