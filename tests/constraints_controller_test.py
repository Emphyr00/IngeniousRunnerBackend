import unittest
from app.block import Block
from app.field import Field
from app.constraint_controllers.constraints_controller import ConstraintsController

class ConstraintsControllerTest (unittest.TestCase):
    def test_create(self):
        block = Block()
        cc = ConstraintsController()
        
        self.assertIsInstance(cc, ConstraintsController)
        
    def test_getEntropy(self):
        block = Block()
        cc = ConstraintsController()

        self.assertEqual(cc.getEntropy(), 8)
        